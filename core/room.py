class Room:
	def __init__(self, room_number):
		self.room_number = room_number
		self.capacity = 8
		self.soldiers = []

	def has_space(self):
		return len(self.soldiers) < self.capacity

	def add_soldier(self, soldier):
		if self.has_space():
			self.soldiers.append(soldier)
			return True
		return False
