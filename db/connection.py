import sqlite3

# DB_CONFIG = {
#     "driver": "{ODBC Driver 17 for SQL Server}",
#     "server": "DESKTOP-M70SVI6\\SQLEXPRESS",
#     "database": "soldier_courses_db",
#     "trusted": "yes"
# }


def get_connection():
	conn = sqlite3.connect(DB_PATH)
	conn.row_factory = sqlite3.Row
	return conn
