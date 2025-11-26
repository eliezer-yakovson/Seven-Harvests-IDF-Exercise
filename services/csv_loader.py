import csv
from core.solider import Soldier 


def load_soldiers_from_csv(file):
	soldiers = []
	lines = file.stream.read().splitlines()
	reader = csv.DictReader(lines)

	for row in reader:
		soldiers.append(
			Soldier(
				personal_id=row["מספר אישי"],
				first_name=row["שם פרטי"],
				last_name=row["שם משפחה"],
				gender=row["מין"],
				city=row["עיר מגורים"],
				distance_km=int(row["מרחק מהבסיס"]),
				status=False
			)
		)
	return soldiers

