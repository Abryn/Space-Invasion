# Import the Pygame library.
import pygame
from pygame.sprite import Sprite

# Create the Player class.
class Life(Sprite):

	def __init__(self, space_invasion):

		super().__init__()

		self.screen = space_invasion.screen
		
		# Assign the settings to an attribute of the Player class.
		self.settings = space_invasion.settings
		
		# Set the rect attribute of the screen.
		self.screen_rect = space_invasion.screen.get_rect()

		# Load the player image and hitbox.
		self.image = pygame.image.load('images/life.png')

		# Set the rect attribute of the player.
		self.rect = self.image.get_rect()

		# Starting position.
		self.rect.center = self.screen_rect.midbottom = (600, 700)

		# Store the x position of the player as a decimal value.
		self.x = float(self.rect.x)

	# Method to display the player.
	def blitplayer(self):
		"""Display the player."""

		# Copy the player image to the player rectangle.
		self.screen.blit(self.image, self.rect)