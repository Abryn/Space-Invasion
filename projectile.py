# Import the Pygame library.
import pygame

# Import the Sprite class from the pygame.sprite module.
from pygame.sprite import Sprite

# Create the Projectile Sprite class.
class Projectile(Sprite):
	"""A class to manage the player's projectiles."""

	# Initialize the class.
	def __init__(self, space_invasion):
		"""Create a projectile at the player's position."""

		# Inherit from the Sprite Class.
		super().__init__()

		# Set an attribute for the settings.
		self.settings = space_invasion.settings

		# Set an attribute for the screen.
		self.screen = space_invasion.screen

		# Set an attribute for the projectile color.
		self.color = self.settings.player_projectile_color

		# Create a projectile rectangle at position (0, 0).
		self.rect = pygame.Rect(0, 0, self.settings.player_projectile_width, self.settings.player_projectile_height)

		# Change the projectile position to where it is being fired from.
		self.rect.midbottom = space_invasion.player.rect.midtop

		# Store the y position of the projectile as a decimal.
		self.y = float(self.rect.y)

	# Method for drawing projectile.
	def draw_projectile(self):
		"""Display the projectile to the screen."""

		# Draw rectangle on the screen with the given color.
		pygame.draw.rect(self.screen, self.color, self.rect)

	# Method for updating positions.
	def update(self):
		"""Move the projectile vertically."""

		# Update the y position of the projectile.
		self.y -= self.settings.player_projectile_speed
		
		# Update the position of the rectangle.
		self.rect.y = self.y
