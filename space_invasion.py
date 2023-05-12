# Imports
import pygame

import sys

from time import sleep

from start import Start

from settings import Settings

from stats import Stats

from score import Score

from player import Player

from projectile import Projectile

from invader import Invader

import random

# Create the main game class.
class SpaceInvasion:
	"""A class to manage the game assets and behavior."""

	# Initialize the class.
	def __init__(self):
		"""Initializing the game and creating game resources."""

		# Initializing Pygame.
		pygame.init()

		# Clock to manipulate the framerate.
		self.clock = pygame.time.Clock()

		# Create an instance of the Settings class.
		self.settings = Settings()

		# Create an instance of the Stats class.
		self.stats = Stats(self)

		# Display the screen size.
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		# Set the game caption.
		pygame.display.set_caption("Space Invasion")

		# Change the background to selected background.
		self.background_color = self.settings.background_color

		# Create an instance of the Player class.
		self.player = Player(self)

		# Create a group for the projectiles.
		self.projectiles = pygame.sprite.Group()

		# Create a group for the invaders.
		self.invaders = pygame.sprite.Group()

		self.score = Score(self)

		# Create the first wave of invaders.
		self._create_wave()

		# Make the start button.
		self.start_button = Start(self, "START")
		
		self.invader_projectile_timer = pygame.time.get_ticks()


	# Method to run the game.
	def run_game(self):
		"""The main loop for the game."""

		# Loop that runs while the game is active.
		while True:
			# Watch for peripheral events.
			self._check_events()

			with open('scores.txt', 'w') as s:
				for score in self.score.highscores:
					s.write(str(score) + "\n")
				s.write("finished")

			if self.stats.active:
				# Update player position.
				self.player.update_position()

				# Update the projectiles position and existance.
				self._update_projectiles()

				# Update the invaders position and existance.
				self._update_invaders()

			# Visualize the most recent screen, updates the screen.
			self._update_screen()

	# Helper method to check for player input.
	def _check_events(self):
		"""Respond to peripheral events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()
				self._check_start_game(mouse_position)

			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup(event)

	def _check_start_game(self, mouse_position):
		if self.start_button.rect.collidepoint(mouse_position) and not self.stats.active:
			pygame.mouse.set_visible(False)
			self.stats.reset_stats()
			self.stats.active = True
			self.settings.default_settings()
			self.score.create_score()
			self.score.create_level()
			self.score.create_lives()

			self.invaders.empty()
			self.projectiles.empty()

			self._create_wave()
			self.player.center_player()

	# Helper method to respond to keys being down.
	def _check_keydown(self, event):
		"""Respond if a key is down."""
		if self.stats.active:
			# Check if the key "d" or "right-arrow" is down.
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				# Move the player to the right.
				self.player.moving_right = True
			# Check if the key "a" or "left-arrow" is down.
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				# Move the player to the left.
				self.player.moving_left = True

			# Check if the key "space" is down.
			if event.key == pygame.K_SPACE:
				# Fire a player projectile.
				self._fire_projectile()

		# Check if the key "q" is down.
		if event.key == pygame.K_ESCAPE:
			# Deactivate the Pygame library.
			pygame.quit()
			# Exit Python.
			sys.exit()

	# Helper method to respond to keys being up.
	def _check_keyup(self, event):
		"""Respond if a key is up."""

		# Check if the key "d" or "right" is up.
		if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
			# Stop the player movement to the right.
			self.player.moving_right = False
		# Check if the key "a" or "left-arrow" is up.
		if event.key == pygame.K_a or event.key == pygame.K_LEFT:
			# Stop the player movement to the left.
			self.player.moving_left = False

	# Helper method for spawning projectiles.
	def _fire_projectile(self):
		"""Create a projectile and add it to the group."""

		# Check if the projectiles are under the projectile limit.
		if len(self.projectiles) < self.settings.player_projectile_limit:
			# Create an instance of the Projectile class.
			projectile = Projectile(self)
			# Add the Projectile instance to a group.
			self.projectiles.add(projectile)

	def _check_projectile_hit(self):
		hits = pygame.sprite.groupcollide(self.projectiles, self.invaders, self.player.normal, True)
		random_power = random.randint(0, 4)

		if hits:
			for invaders in hits.values():
				self.stats.score += self.settings.invader_value * len(invaders)
				
				if random_power == 1:
					self.player.power_up()
			
			self.score.create_score()
			self.score.check_high_score()

		if not self.invaders:
			self.projectiles.empty()
			self._create_wave()
			self.settings.difficulty_increase()
			self.stats.level += 1
			self.score.create_level()


	# Helper method for updating projectiles.
	def _update_projectiles(self):
		"""Update position of the projectiles and remove projectiles past the screen."""

		# Update the projectiles position.
		self.projectiles.update()
		self.score.create_projectiles()

		self._check_projectile_hit()

		# Loop that loops over every projectile in a copy of the projectiles group.
		for projectile in self.projectiles.copy():
			# Check if projectile is off the screen.
			if projectile.rect.bottom <= 0:
				# Remove the projectile once it is off the screen.
				self.projectiles.remove(projectile)

	# Helper method for creating many invaders.
	def _create_wave(self):
		"""Create invaders."""
		# Make an invader.
		invader = Invader(self)
		invader_width = invader.rect.width
		invader_height = invader.rect.height
		player_height = self.player.rect.height
		screen_width = self.settings.screen_width - (2 * invader_width)
		screen_height = self.settings.screen_height - (3 * invader_height) - player_height
		invader_amount_x = screen_width // (2 * invader_width)
		invader_amount_y = screen_width // (4 * invader_height)

		for rows in range(invader_amount_x):
			for cols in range(invader_amount_y):
				self._create_invader(rows, cols)

	# Helper method for creating an invader.
	def _create_invader(self, rows, cols):
		# Make an invader.
		invader = Invader(self)
		invader_width, invader_height = invader.rect.size
		invader.x = invader_width + 2 * invader_width * rows
		invader.rect.x = invader.x
		invader.rect.y = invader_height + 2 * invader.rect.height * cols
		self.invaders.add(invader) 


	def _check_wave_borders(self):
		for invader in self.invaders.sprites():
			if invader.check_borders():
				self._change_wave_direction()
				break

	def _change_wave_direction(self):
		for invader in self.invaders.sprites():
			invader.rect.y += self.settings.wave_drop_distance
		self.settings.wave_direction *= -1

	def _game_over(self):
		if self.stats.players_left > 0:
			self.stats.players_left -= 1
			self.score.create_lives()

			self.invaders.empty()
			self.projectiles.empty()

			self._create_wave()
			self.player.center_player()

			sleep(0.5)
		else:
			pygame.mouse.set_visible(True)
			self.stats.active = False

	def _check_invader_win(self):
		screen_rect = self.screen.get_rect()
		for invader in self.invaders.sprites():
			if invader.rect.bottom >= screen_rect.bottom:
				self._game_over()
				break

	# Helper method for updating invaders.
	def _update_invaders(self):
		"""Update the position of the invaders"""
		self._check_wave_borders()
		self.invaders.update()
		self._check_invader_win()
		if pygame.sprite.spritecollideany(self.player, self.invaders):
			self._game_over()

	# Helper method for updating the screen.
	def _update_screen(self):
		"""Update stuff on the screen."""
		# Fill the screen with the background color.
		self.screen.fill(self.background_color)

		# Copy the player image file to the player rectangle.
		self.player.blitplayer()

		# Loop over each projectile in the projectiles sprite group.
		for projectile in self.projectiles.sprites():
			# Draw the projectile.
			projectile.draw_projectile()

		# Draw the invaders.
		self.invaders.draw(self.screen)

		self.score.display_score()

		# Draw the start button if game is not active.
		if not self.stats.active:
			self.start_button.draw_start()

		# Update the full display to the screen.
		pygame.display.flip()

		# Update the clock.
		self.clock.tick(self.settings.fps)
			
# Check if the file is run directly.
if __name__ == "__main__":
	# Make an instance of the game class.
	space_invasion = SpaceInvasion()

	# Run the game class.
	space_invasion.run_game()