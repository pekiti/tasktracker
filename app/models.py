from datetime import datetime
from app.database import get_db

"""
Task data model and database operations.

Implements Task class with static methods for CRUD operations:
- Create new tasks
- Retrieve all or pending tasks
- Mark tasks as completed
- Delete tasks

Class Methods:
    create_task(title, description, due_date)
    get_all_tasks()
    get_pending_tasks()
    mark_completed(task_id)
    delete_task(task_id)
"""

class Task:
    @staticmethod
    def create_task(title, description, due_date):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)',
            (title, description, due_date)
        )
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all_tasks():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM tasks ORDER BY due_date')
        return cursor.fetchall()

    @staticmethod
    def get_pending_tasks():
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'SELECT * FROM tasks WHERE completed = 0 AND due_date <= ? ORDER BY due_date',
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),)
        )
        return cursor.fetchall()

    @staticmethod
    def mark_completed(task_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        db.commit()

    @staticmethod
    def delete_task(task_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        db.commit() 