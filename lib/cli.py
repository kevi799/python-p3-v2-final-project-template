import sqlite3
import click
from models.User import User  

# Function to get the database connection
def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect("budget_tracker.db")

# Initialize the database and create tables if they don't exist
def init_db():
    """Initialize the database by creating necessary tables if they don't exist."""
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
    click.echo("Database initialized successfully!")

# CLI group for the application
@click.group()
def cli():
    """CLI for managing the Personal Budget Tracker application."""
    click.echo("Personal Budget Tracker CLI")

# Ensure the database is initialized when running the CLI
init_db()

# Subcommand for user management
@cli.group()
def user():
    """Manage users"""
    pass

# Command to add a new user
@user.command()
def add():
    """Add a new user"""
    name = click.prompt("Enter your name")
    email = click.prompt("Enter your email")
    password = click.prompt("Enter your password", hide_input=True)
    
    # Hash the password (assuming User class handles password hashing)
    hashed_password = User.hash_password(password)  
    
    # Get a connection to the database
    connection = get_connection()
    cursor = connection.cursor()
    
    # Insert the new user into the users table
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                       (name, email, hashed_password))
        connection.commit()
        click.echo(f"User {name} added successfully!")
    except sqlite3.IntegrityError:
        click.echo(f"Error: User with email {email} already exists.")
    finally:
        connection.close()

# Command to view all users
@user.command()
def view():
    """View all users"""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    
    if users:
        click.echo(f"{'ID':<5} {'Name':<20} {'Email':<30}")
        click.echo("-" * 60)
        for user in users:
            click.echo(f"{user[0]:<5} {user[1]:<20} {user[2]:<30}")
    else:
        click.echo("No users found.")
    
    connection.close()

# Command to delete a user by ID
@user.command()
@click.argument('user_id', type=int)
def delete(user_id):
    """Delete a user by their ID"""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    if cursor.rowcount > 0:
        connection.commit()
        click.echo(f"User with ID {user_id} deleted successfully!")
    else:
        click.echo(f"Error: User with ID {user_id} not found.")
    
    connection.close()

# Subcommand for managing budgets
@cli.group()
def budget():
    """Manage budgets"""
    pass

# Command to add a budget (simple example)
@budget.command()
def add():
    """Add a new budget"""
    user_id = click.prompt("Enter user ID", type=int)
    amount = click.prompt("Enter the budget amount", type=float)
    
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO budgets (user_id, amount) VALUES (?, ?)", (user_id, amount))
    connection.commit()
    connection.close()
    
    click.echo(f"Budget of {amount} added for user {user_id}!")

# Command to view all budgets
@budget.command()
def view():
    """View all budgets"""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, user_id, amount FROM budgets")
    budgets = cursor.fetchall()
    
    if budgets:
        click.echo(f"{'ID':<5} {'User ID':<10} {'Amount':<10}")
        click.echo("-" * 30)
        for budget in budgets:
            click.echo(f"{budget[0]:<5} {budget[1]:<10} {budget[2]:<10}")
    else:
        click.echo("No budgets found.")
    
    connection.close()

# Command to delete a budget by ID
@budget.command()
@click.argument('budget_id', type=int)
def delete(budget_id):
    """Delete a budget by its ID"""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM budgets WHERE id = ?", (budget_id,))
    if cursor.rowcount > 0:
        connection.commit()
        click.echo(f"Budget with ID {budget_id} deleted successfully!")
    else:
        click.echo(f"Error: Budget with ID {budget_id} not found.")
    
    connection.close()

# Subcommand for managing expenses
@cli.group()
def expense():
    """Manage expenses"""
    pass

# Command   to add an expense
@expense.command()
def add():
    """Add a new expense"""
    user_id = click.prompt("Enter user ID", type=int)
    amount = click.prompt("Enter the expense amount", type=float)
    description = click.prompt("Enter the expense description")
    date = click.prompt("Enter the expense date (YYYY-MM-DD)")
    
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO expenses (user_id, amount, description, date) VALUES (?, ?, ?, ?)",
                   (user_id, amount, description, date))
    connection.commit()
    connection.close()
    
    click.echo(f"Expense of {amount} added for user {user_id} on {date}.")

# Command to view all expenses
@expense.command()
def view():
    """View all expenses"""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, user_id, amount, description, date FROM expenses")
    expenses = cursor.fetchall()
    
    if expenses:
        click.echo(f"{'ID':<5} {'User ID':<10} {'Amount':<10} {'Description':<30} {'Date':<10}")
        click.echo("-" * 70)
        for expense in expenses:
            click.echo(f"{expense[0]:<5} {expense[1]:<10} {expense[2]:<10} {expense[3]:<30} {expense[4]:<10}")
    else:
        click.echo("No expenses found.")
    
    connection.close()

# Main entry point
if __name__ == "__main__":
    cli()
