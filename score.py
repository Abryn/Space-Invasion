import pygame.font

from pygame.sprite import Group

from life import Life

from player import Player

class Score:
	"""Class for the score system."""
	def __init__(self, space_invasion):
		self.space_invasion = space_invasion
		self.screen = space_invasion.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = space_invasion.settings
		self.stats = space_invasion.stats
		self.player = space_invasion.player

		self.text_color = (255, 255, 255)
		self.special_color = (135, 235, 255)
		self.font = pygame.font.Font("fonts/pixel.ttf", 30)

		self.highscores = []

		self.create_score()
		self.create_high_score()
		self.create_level()
		self.create_projectiles()
		self.create_lives()
		self.create_power()

	def create_score(self):
		rounded_score = round(self.stats.score, -1)
		score_string = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_string, True, self.text_color, self.settings.background_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.centerx = self.screen_rect.centerx
		self.score_rect.top = 0

	def create_high_score(self):
		high_score = round(self.stats.high_score, -1)
		high_score_string = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_string, True, self.special_color, self.settings.background_color)

		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.right - 10
		self.high_score_rect.top = self.screen_rect.bottom - 50

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.create_high_score()
			self.highscores.append(self.stats.high_score)

	def create_level(self):
		level_string = "WAVE: " + str(self.stats.level)
		self.level_image = self.font.render(level_string, True, self.text_color, self.settings.background_color)

		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 10
		self.level_rect.top = 0

	def create_projectiles(self):
		projectiles_string = str(self.settings.player_projectile_limit - len(self.space_invasion.projectiles))
		self.projectiles_image = self.font.render(projectiles_string, True, self.special_color, self.settings.background_color)

		self.projectiles_rect = self.projectiles_image.get_rect()
		self.projectiles_rect.left = self.player.x + 42
		self.projectiles_rect.top = self.screen_rect.bottom - 55

	def create_lives(self):
		self.players = Group()
		for player_number in range(self.stats.players_left):
			player = Life(self.space_invasion)
			player.rect.x = 10 + player_number * player.rect.width
			player.rect.y = 10
			self.players.add(player)

	def create_power(self):
		power_string = "POWER UP"
		self.power_image = self.font.render(power_string, True, self.special_color, self.settings.background_color)
		self.power_rect = self.power_image.get_rect()
		self.power_rect.left = self.screen_rect.left + 150
		self.power_rect.top = 0

	def display_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.projectiles_image, self.projectiles_rect)
		if not self.player.normal:
			self.screen.blit(self.power_image, self.power_rect)
		self.players.draw(self.screen)


