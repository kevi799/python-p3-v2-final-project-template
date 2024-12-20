import click
from helpers import get_connection
from models.User import User
from models.Budget import Budget
from models.Expense import Expense

@click.group()
def cli():

    pass

@cli.group()
def user():

    pass

@user.command("add")
def add_user():
 
    name = click.prompt("Enter your name")
    email = click.prompt("Enter your email")
    password = click.prompt("Enter your password", hide_input=True) 

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
def add_budget():
    """Add a budget."""
    user_id = click.prompt("Enter user ID", type=int)
    amount = click.prompt("Enter budget amount", type=float)

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
def update_budget():
    """Update a user's budget."""
    user_id = click.prompt("Enter user ID", type=int)
    amount = click.prompt("Enter new budget amount", type=float)

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
def add_expense():
    """Add an expense."""
    user_id = click.prompt("Enter user ID", type=int)
    amount = click.prompt("Enter expense amount", type=float)
    description = click.prompt("Enter expense description")
    date = click.prompt("Enter expense date (YYYY-MM-DD)")

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
def update_expense():
    """Update an expense."""
    expense_id = click.prompt("Enter expense ID", type=int)
    amount = click.prompt("Enter new amount", type=float)
    description = click.prompt("Enter new description")
    date = click.prompt("Enter new date (YYYY-MM-DD)")

    Expense.update(expense_id, amount=amount, description=description, date=date)
    click.echo("Expense updated successfully!")

if __name__ == "__main__":
    cli()
