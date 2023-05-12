import pygame

import threading

from projectile import Projectile

# Create the Player class.
class Player:
	"""A class to manage the player's player."""

	# Initialize the class.
	def __init__(self, space_invasion):
		"""Initialize the player player."""

		# Assign the screen to an attribute of the Player class.
		self.screen = space_invasion.screen
		
		# Assign the settings to an attribute of the Player class.
		self.settings = space_invasion.settings
		
		# Set the rect attribute of the screen.
		self.screen_rect = space_invasion.screen.get_rect()

		# Load the player image and hitbox.
		self.image = pygame.image.load('images/player.png')

		# Set the rect attribute of the player.
		self.rect = self.image.get_rect()

		# Starting position.
		self.rect.center = self.screen_rect.midbottom = (600, 700)

		# Store the x position of the player as a decimal value.
		self.x = float(self.rect.x)
		
		self.moving_right = False

		self.moving_left = False

		self.projectile_default_height = self.settings.player_projectile_height

		self.projectile_default_width = self.settings.player_projectile_width

		self.default_player_speed = self.settings.player_speed

		self.normal = True

	def center_player(self):
		self.rect.center = self.screen_rect.midbottom = (600, 700)
		self.x = float(self.rect.x)

	# Method to update player position.
	def update_position(self):
		"""Update the position of the player based on the movement flags."""

		# Check if player is moving right and is within the screen.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			# Move the player right horizontally with the player speed.
			self.x += self.settings.player_speed
		# Check if player is moving left and is within the screen.
		if self.moving_left and self.rect.left > self.screen_rect.left:
			# Move the player left horizontally with player speed.
			self.x -= self.settings.player_speed

		# Updating the players position.
		self.rect.x = self.x

	def power_up(self):
		if self.normal:	
			self.normal = False
			self.settings.player_projectile_height = 1000
			self.settings.player_projectile_width = 50
			self.settings.player_speed *= 2

		def reset_power_up():
			if not self.normal:
				self.normal = True
				self.settings.player_projectile_height = self.projectile_default_height
				self.settings.player_projectile_width = self.projectile_default_width
				self.settings.player_speed /= 2
	
		timer = threading.Timer(2.0, reset_power_up)
		timer.start()



	# Method to display the player.
	def blitplayer(self):
		"""Display the player."""

		# Copy the player image to the player rectangle.
		self.screen.blit(self.image, self.rect)