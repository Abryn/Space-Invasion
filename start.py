import pygame.font

class Start:
	"""Class for the start button."""
	def __init__(self, space_invasion, msg):
		self.screen = space_invasion.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 140, 50
		self.start_color = (255, 30, 30)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.Font("fonts/pixel.ttf", 30)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self._create_msg(msg)

	def _create_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.start_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		self.msg_image_rect.right += 2
		self.msg_image_rect.top -= 2

	def draw_start(self):
		self.screen.fill(self.start_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)