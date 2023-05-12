# Import the Pygame library.
import pygame

# Import the Sprite class from the pygame.sprite module.
from pygame.sprite import Sprite

# Create the Invader Sprite class.
class Invader(Sprite):
	"""A class to manage each invader in the game."""

	# Initialize the class.
	def __init__(self, space_invasion):
		"""Initialize the invader."""

		# Inherit from the Sprite Class.
		super().__init__()

		# Assign the screen to an attribute of the Invader class.
		self.screen = space_invasion.screen

		# Assign the settings to an attribute of the Invader class.
		self.settings = space_invasion.settings

		# Load the image representing the invader.
		self.image = pygame.image.load("images/invader.png")

		# Set the rect attribute of the invader.
		self.rect = self.image.get_rect()

		self.rect.x = 52

		self.rect.y = 52

		# Store the x position of the invader as a decimal.
		self.x = float(self.rect.x)

	def check_borders(self):
		"""Return true when an alien is at the border of the screen."""
		screen = self.screen.get_rect()

		if self.rect.right >= screen.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Move the alien."""
		self.x += (self.settings.invader_speed * self.settings.wave_direction)
		self.rect.x = self.x
