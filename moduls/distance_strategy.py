class DistanceStrategy():
	def sort_soldiers(self, soldiers):
		return sorted(soldiers, key=lambda s: s.distance_km)
