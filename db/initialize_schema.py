from db.connection import get_connection


def initialize_schema():
	conn = get_connection()
	cur = conn.cursor()

	cur.executescript("""

	DROP TABLE IF EXISTS soldiers;
	DROP TABLE IF EXISTS dorms;
	DROP TABLE IF EXISTS rooms;
	DROP TABLE IF EXISTS assignments;
	DROP TABLE IF EXISTS waiting_list;

	CREATE TABLE soldiers (
		personal_id TEXT PRIMARY KEY,
		first_name TEXT,
		last_name TEXT,
		gender TEXT,
		city TEXT,
		distance_km INTEGER,
		status TEXT,
	);

	CREATE TABLE dorms (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT
	);

	CREATE TABLE rooms (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		dorm_id INTEGER,
		room_number INTEGER,
		capacity INTEGER DEFAULT 8,
		FOREIGN KEY(dorm_id) REFERENCES dorms(id)
	);

	CREATE TABLE assignments (
		soldier_id TEXT,
		dorm_id INTEGER,
		room_id INTEGER,
		PRIMARY KEY(soldier_id),
		FOREIGN KEY(soldier_id) REFERENCES soldiers(personal_id),
		FOREIGN KEY(room_id) REFERENCES rooms(id),
		FOREIGN KEY(dorm_id) REFERENCES dorms(id)
	);

	CREATE TABLE waiting_list (
		soldier_id TEXT PRIMARY KEY,
		FOREIGN KEY(soldier_id) REFERENCES soldiers(personal_id)
	);

	""")

	cur.execute("INSERT INTO dorms (name) VALUES ('A')")
	cur.execute("INSERT INTO dorms (name) VALUES ('B')")

	for dorm_id in [1, 2]:
		for room_number in range(1, 11):
			cur.execute(
				"""
				INSERT INTO rooms (dorm_id, room_number)
				VALUES (?, ?)
				""",
				(dorm_id, room_number),
			)

	conn.commit()
	conn.close()
	return True
