from flask import Blueprint, jsonify, request
from services.csv_loader import load_soldiers_from_csv
from repository.sql_repo import SQLRepo
from core.distance_strategy import DistanceStrategy


assign_bp = Blueprint("assign", __name__)
repo = SQLRepo()
strategy = DistanceStrategy()


@assign_bp.post("/assignWithCsv")
def assign_with_csv():
	file = request.files["file"]
	soldiers = load_soldiers_from_csv(file)

	for soldier in soldiers:
		repo.insert_soldier(soldier)

	ordered = strategy.sort_soldiers(soldiers)

	assigned = 0
	waiting = 0

	for soldier in ordered:
		room = repo.get_available_room()
		if room:
			repo.assign_soldier(soldier.personal_id, room["dorm_id"], room["id"])
			assigned += 1
		else:
			repo.add_to_waiting_list(soldier.personal_id)
			waiting += 1

	return jsonify({"assigned": assigned, "waiting": waiting})
