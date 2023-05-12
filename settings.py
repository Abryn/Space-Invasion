# Create the Settings class.
class Settings:
	"""A class to store the user settings for Space Invasion."""

	# Initialize the class.
	def __init__(self):
		"""Initialize the settings."""
		self.screen_width = 1200

		self.screen_height = 800

		self.background_color = (20, 20, 20)
		
		self.player_speed = 1.5

		self.fps = 144

		self.player_projectile_width = 4

		self.player_projectile_height = 10

		self.player_projectile_speed = 3.0

		self.player_projectile_limit = 3

		self.player_projectile_color = (135, 235, 255)

		self.player_limit = 3

		self.invader_speed = 10.0

		self.wave_drop_distance = 10

		self.wave_direction = 1

		self.invader_value = 50

		# Difficulty settings.
		self.speed_increment = 1.2

		self.score_increment = 1.5

		self.default_settings()

	def default_settings(self):
		self.player_speed = 1.5
		self.player_projectile_speed = 3.0
		self.invader_speed = 1.0
		self.wave_direction = 1
		self.invader_value = 50

	def difficulty_increase(self):
		self.player_speed *= self.speed_increment
		self.player_projectile_speed *= self.speed_increment
		self.invader_speed *= self.speed_increment
		self.invader_value = int(self.invader_value * self.score_increment)