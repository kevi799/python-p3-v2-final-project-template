# models/Expense.py
from helpers import get_connection
class Expense:
    def __init__(self, id, user_id, amount, description, date):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Expense(ID: {self.id}, User ID: {self.user_id}, Amount: {self.amount}, Description: {self.description}, Date: {self.date})"

    @classmethod
    def save(cls, user_id, amount, description, date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (user_id, amount, description, date) VALUES (?, ?, ?, ?)", 
                       (user_id, amount, description, date))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        conn.close()
        return [Expense(*row) for row in rows]

    @classmethod
    def delete(cls, expense_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, expense_id, amount=None, description=None, date=None):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE expenses SET "
        params = []
        if amount:
            query += "amount = ?, "
            params.append(amount)
        if description:
            query += "description = ?, "
            params.append(description)
        if date:
            query += "date = ?, "
            params.append(date)
        query = query.rstrip(", ")  # Remove the trailing comma
        query += " WHERE id = ?"
        params.append(expense_id)
        cursor.execute(query, tuple(params))
        conn.commit()
        conn.close()
