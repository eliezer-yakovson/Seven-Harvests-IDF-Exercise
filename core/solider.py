class Soldier:
	def __init__(self, personal_id, first_name, last_name,
				 gender, city, distance_km, status):
		self.personal_id = personal_id
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.city = city
		self.distance_km = distance_km
		self.status = status  
	
		self.assigned = False
		self.dorm = None
		self.room = None