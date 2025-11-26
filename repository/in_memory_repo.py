class InMemoryRepo:
	def __init__(self, dorms, waiting_list):
		self.soldiers = []
		self.dorms = dorms
		self.waiting_list = waiting_list

	def add_soldier(self, soldier):
		self.soldiers.append(soldier)

	def get_soldier(self, pid):
		return next((s for s in self.soldiers if s.personal_id == pid), None)

	def get_waiting_list(self):
		return self.waiting_list

	def get_space_report(self):
		report = {}
		for dorm in self.dorms:
			full = sum(len(room.soldiers) for room in dorm.rooms)
			empty = 80 - full
			report[dorm.dorm_name] = {
				"full": full,
				"empty": empty
			}
		return report
