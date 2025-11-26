class AssignmentManager:
	def __init__(self, dorms, strategy):
		self.dorms = dorms
		self.strategy = strategy
		self.waiting_list = []

	def assign_soldiers(self, soldiers):
		ordered = self.strategy.sort_soldiers(soldiers)

		for soldier in ordered:
			placed = False

			for dorm in self.dorms:
				room_num = dorm.assign(soldier)
				if room_num:
					soldier.assigned = True
					soldier.dorm = dorm.dorm_name
					soldier.room = room_num
					placed = True
					break

			if not placed:
				self.waiting_list.append(soldier)
