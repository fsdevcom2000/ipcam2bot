import sqlite3


class CameraRepository:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init()

    def _init(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cameras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                url TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def add(self, user_id: int, name: str, url: str):
        self.conn.execute(
            "INSERT INTO cameras (user_id, name, url) VALUES (?, ?, ?)",
            (user_id, name, url)
        )
        self.conn.commit()

    def delete(self, user_id: int, camera_id: int):
        self.conn.execute(
            "DELETE FROM cameras WHERE id = ? AND user_id = ?",
            (camera_id, user_id)
        )
        self.conn.commit()

    def list_by_user(self, user_id: int):
        cur = self.conn.execute(
            "SELECT * FROM cameras WHERE user_id = ?",
            (user_id,)
        )
        return cur.fetchall()

    def list_all(self):
        return self.conn.execute("SELECT * FROM cameras").fetchall()