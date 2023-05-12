class Stats():
	def __init__(self, space_invasion):
		self.active = False
		self.settings = space_invasion.settings
		self.reset_stats()
		self.high_score = 0

	def reset_stats(self):
		self.players_left = self.settings.player_limit
		self.score = 0
		self.level = 1