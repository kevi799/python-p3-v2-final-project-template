import sqlite3
import os

def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect("budget_tracker.db")

def init_db():
    """Initialize the database by creating the necessary tables if they don't exist."""
    if not os.path.exists("budget_tracker.db"):
        print("Database file not found. Creating a new one...")

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Enable foreign key constraints (SQLite requires explicit enabling)
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # Create Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """)

        # Create Budgets table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        """)

        # Create Expenses table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        """)

        # Commit changes and close connection
        connection.commit()
        connection.close()
        print("Database initialized successfully!")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        if connection:
            connection.rollback()
    finally:
        if connection:
            connection.close()

# Call the function to create tables if they don't exist
if __name__ == "__main__":
    init_db()
