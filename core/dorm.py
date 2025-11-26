from .room import Room


class Dorm:
	def __init__(self, dorm_name):
		self.dorm_name = dorm_name
		self.rooms = [Room(i) for i in range(1, 11)]  

	def assign(self, soldier):
		for room in self.rooms:
			if room.add_soldier(soldier):
				return room.room_number
		return None
