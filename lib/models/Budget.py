import sqlite3
from datetime import datetime

class Budget:
    def __init__(self, id, user_id, amount, category, created_at=None, updated_at=None):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __repr__(self):
        return f"Budget(ID: {self.id}, User ID: {self.user_id}, Amount: {self.amount}, Category: {self.category}, Created At: {self.created_at}, Updated At: {self.updated_at})"

    @classmethod
    def create_table(cls):
        """Creates the Budget table in the database."""
        conn = sqlite3.connect('your_database.db')#####
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL,
                category TEXT,
                created_at TEXT,
                updated_at TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.commit()
        conn.close()

    @classmethod
    def save(cls, user_id, amount, category):
        """Inserts a new budget entry into the database."""
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        created_at = updated_at = datetime.now()
        cursor.execute("""
            INSERT INTO budgets (user_id, amount, category, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, amount, category, created_at, updated_at))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Fetches all budget entries from the database."""
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM budgets")
        rows = cursor.fetchall()
        conn.close()
        return [cls(*row) for row in rows]

    @classmethod
    def get_by_id(cls, budget_id):
        """Fetches a budget entry by its ID."""
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM budgets WHERE id = ?", (budget_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(*row) if row else None

    @classmethod
    def update(cls, budget_id, amount=None, category=None):
        """Updates an existing budget entry."""
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        updated_at = datetime.now()
        if amount:
            cursor.execute("UPDATE budgets SET amount = ?, updated_at = ? WHERE id = ?", (amount, updated_at, budget_id))
        if category:
            cursor.execute("UPDATE budgets SET category = ?, updated_at = ? WHERE id = ?", (category, updated_at, budget_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, budget_id):
        """Deletes a budget entry by its ID."""
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM budgets WHERE id = ?", (budget_id,))
        conn.commit()
        conn.close()
