import click
from helpers import get_connection
from models.User import User
from models.Budget import Budget

# User CLI Commands
@click.group()
def cli():
    """Budget Tracker CLI"""
    pass

# User CLI Group
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

# Budget CLI Group
@cli.group()
def budget():
    """Manage budgets."""
    pass

@budget.command("add")
@click.argument("user_id", type=int)
@click.argument("amount", type=float)
@click.argument("category")
def add_budget(user_id, amount, category):
    """Add a new budget."""
    Budget.save(user_id, amount, category)
    click.echo("Budget added successfully!")

@budget.command("view")
def view_budgets():
    """View all budgets."""
    budgets = Budget.get_all()
    if budgets:
        for budget in budgets:
            click.echo(budget)
    else:
        click.echo("No budgets found.")

@budget.command("delete")
@click.argument("budget_id", type=int)
def delete_budget(budget_id):
    """Delete a budget."""
    Budget.delete(budget_id)
    click.echo("Budget deleted successfully.")

@budget.command("update")
@click.argument("budget_id", type=int)
@click.option("--amount", type=float, help="New amount")
@click.option("--category", type=str, help="New category")
def update_budget(budget_id, amount, category):
    """Update an existing budget."""
    Budget.update(budget_id, amount=amount, category=category)
    click.echo("Budget updated successfully.")

if __name__ == '__main__':
    cli()
