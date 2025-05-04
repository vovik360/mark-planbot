import sqlite3
from datetime import datetime

def init_db():
    with sqlite3.connect("tasks.db") as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT,
                due_time TEXT,
                notified INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

def save_task(user_id: int, text: str, due_time: datetime) -> int:
    with sqlite3.connect("tasks.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tasks (user_id, text, due_time) VALUES (?, ?, ?)",
                  (user_id, text, due_time.isoformat()))
        conn.commit()
        return c.lastrowid

def get_due_tasks():
    now = datetime.now().isoformat()
    with sqlite3.connect("tasks.db") as conn:
        c = conn.cursor()
        c.execute("SELECT id, user_id, text FROM tasks WHERE due_time <= ? AND notified = 0", (now,))
        return c.fetchall()

def mark_task_notified(task_id: int):
    with sqlite3.connect("tasks.db") as conn:
        c = conn.cursor()
        c.execute("UPDATE tasks SET notified = 1 WHERE id = ?", (task_id,))
        conn.commit()
