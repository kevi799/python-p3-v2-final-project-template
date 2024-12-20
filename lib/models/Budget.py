import sqlite3

class Budget:
    def __init__(self, user_id, amount, id=None):
        self.id = id
        self.user_id = user_id
        self.amount = amount

    @classmethod
    def save(cls, user_id, amount):
        """Save a budget to the database."""
        conn = sqlite3.connect("budget_tracker.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO budgets (user_id, amount) VALUES (?, ?)", (user_id, amount))
        conn.commit()
        conn.close()

    @classmethod
    def get_by_user(cls, user_id):
        """Get a budget by user_id."""
        conn = sqlite3.connect("budget_tracker.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM budgets WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(*row)
        return None

    @classmethod
    def update(cls, user_id, amount):
        """Update the budget for a user."""
        conn = sqlite3.connect("budget_tracker.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE budgets SET amount = ? WHERE user_id = ?", (amount, user_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, user_id):
        """Delete a budget by user_id."""
        conn = sqlite3.connect("budget_tracker.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM budgets WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Get all budgets."""
        conn = sqlite3.connect("budget_tracker.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM budgets")
        rows = cursor.fetchall()
        conn.close()
        return [cls(*row) for row in rows]
