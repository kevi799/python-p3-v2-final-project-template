import click
from helpers import get_connection
from models.User import User
from models.Budget import Budget
from models.Expense import Expense

@click.group()
def cli():
    """Personal Budget Tracker CLI"""
    pass

@cli.group()
def user():
    """Manage users."""
    pass

@user.command("add")
@click.argument("name")
@click.argument("email")
@click.argument("password")
def add_user(name, email, password):
    """Add a new user."""
    hashed_password = User.hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
        conn.commit()
        click.echo("User added successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        conn.close()

@user.command("view")
def view_users():
    """View all users."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            user = User(*row)
            click.echo(user)
    else:
        click.echo("No users found.")

@user.command("delete")
@click.argument("user_id", type=int)
def delete_user(user_id):
    """Delete a user."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    click.echo("User deleted successfully.")


@cli.group()
def budget():
    """Manage budgets."""
    pass

@budget.command("add")
@click.argument("user_id", type=int)
@click.argument("amount", type=float)
def add_budget(user_id, amount):
    """Add a budget."""
    Budget.save(user_id, amount)
    click.echo("Budget added successfully!")

@budget.command("view")
@click.argument("user_id", type=int)
def view_budget(user_id):
    """View the budget for a specific user."""
    budget = Budget.get_by_user(user_id)
    if budget:
        click.echo(budget)
    else:
        click.echo("No budget found for this user.")

@budget.command("update")
@click.argument("user_id", type=int)
@click.argument("amount", type=float)
def update_budget(user_id, amount):
    """Update a user's budget."""
    Budget.update(user_id, amount)
    click.echo("Budget updated successfully!")

@budget.command("delete")
@click.argument("user_id", type=int)
def delete_budget(user_id):
    """Delete a user's budget."""
    Budget.delete(user_id)
    click.echo("Budget deleted successfully.")


@cli.group()
def expense():
    """Manage expenses."""
    pass

@expense.command("add")
@click.argument("user_id", type=int)
@click.argument("amount", type=float)
@click.argument("description")
@click.argument("date")
def add_expense(user_id, amount, description, date):
    """Add an expense."""
    Expense.save(user_id, amount, description, date)
    click.echo("Expense added successfully!")

@expense.command("view")
def view_expenses():
    """View all expenses."""
    expenses = Expense.get_all()
    if expenses:
        for expense in expenses:
            click.echo(expense)
    else:
        click.echo("No expenses found.")

@expense.command("delete")
@click.argument("expense_id", type=int)
def delete_expense(expense_id):
    """Delete an expense."""
    Expense.delete(expense_id)
    click.echo("Expense deleted successfully.")

@expense.command("update")
@click.argument("expense_id", type=int)
@click.option("--amount", type=float, help="Updated amount")
@click.option("--description", help="Updated description")
@click.option("--date", help="Updated date")
def update_expense(expense_id, amount, description, date):
    """Update an expense."""
    Expense.update(expense_id, amount=amount, description=description, date=date)
    click.echo("Expense updated successfully!")

if __name__ == "__main__":
    cli()
