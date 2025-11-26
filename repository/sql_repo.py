from db.connection import get_connection


class SQLRepo:

    def insert_soldier(self, soldier):                                             
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT OR REPLACE INTO soldiers
            (personal_id, first_name, last_name, gender, city, distance_km, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                soldier.personal_id,
                soldier.first_name,
                soldier.last_name,
                soldier.gender,
                soldier.city,
                soldier.distance_km,
                soldier.status
            )
        )

        conn.commit()
        conn.close()

    def assign_soldier(self, soldier_id, dorm_id, room_id):                              
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT OR REPLACE INTO assignments (soldier_id, dorm_id, room_id)
            VALUES (?, ?, ?)
            """,
            (soldier_id, dorm_id, room_id),
        )

        cur.execute("DELETE FROM waiting_list WHERE soldier_id=?", (soldier_id,))

        conn.commit()
        conn.close()

    def add_to_waiting_list(self, soldier_id):                                        
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT OR REPLACE INTO waiting_list (soldier_id)
            VALUES (?)
            """,
            (soldier_id,),
        )

        conn.commit()
        conn.close()

    def get_available_room(self):                                                      
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT rooms.id, rooms.dorm_id
            FROM rooms
            LEFT JOIN assignments ON assignments.room_id = rooms.id
            GROUP BY rooms.id
            HAVING COUNT(assignments.soldier_id) < rooms.capacity
            ORDER BY rooms.id ASC
            LIMIT 1
            """
        )

        result = cur.fetchone()
        conn.close()
        return result

    def get_waiting_list(self):                                                     
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT soldier_id FROM waiting_list
            ORDER BY soldier_id
            """
        )

        rows = cur.fetchall()
        conn.close()

        return [r["soldier_id"] for r in rows]

    def get_space_report(self):                                                       
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
                 SELECT dorms.name AS dorm,
                     rooms.room_number,
                     rooms.capacity,
                     COUNT(assignments.soldier_id) AS used
            FROM rooms
            LEFT JOIN assignments ON assignments.room_id = rooms.id
            LEFT JOIN dorms ON dorms.id = rooms.dorm_id
            GROUP BY rooms.id
            """
        )

        rows = cur.fetchall()
        conn.close()

        summary = {}

        for row in rows:
            dorm_name = row["dorm"]
            if dorm_name is None:
                continue

            summary.setdefault(dorm_name, {"full": 0, "empty": 0})

            if row["used"] < row["capacity"]:
                summary[dorm_name]["empty"] += 1
            else:
                summary[dorm_name]["full"] += 1

        return summary

