import click
from models.User import User
from models.Budget import Budget
from models.Expense import Expense

# Sample in-memory databases (replace with actual database logic)
users = []
budgets = []
expenses = []

@click.group()
def cli():
    """CLI for managing the application"""
    click.echo("Database initialized successfully!")

# User commands
@cli.group()
def user():
    """Manage users"""
    pass

@user.command()
def add():
    """Add a new user"""
    name = click.prompt("Enter your name")
    email = click.prompt("Enter your email")
    password = click.prompt("Enter your password", hide_input=True)
    hashed_password = User.hash_password(password)
    new_user = User(len(users) + 1, name, email, hashed_password)
    users.append(new_user)
    click.echo(f"User {name} added successfully!")

@user.command()
def view():
    """View all users"""
    if users:
        for user in users:
            click.echo(user)
    else:
        click.echo("No users found.")

@user.command()
def remove():
    """Remove a user by ID"""
    user_id = click.prompt("Enter user ID to remove", type=int)
    global users
    users = [u for u in users if u.id != user_id]
    click.echo(f"User with ID {user_id} removed.")

@user.command()
def update():
    """Update a user by ID"""
    user_id = click.prompt("Enter user ID to update", type=int)
    user = next((u for u in users if u.id == user_id), None)
    if user:
        new_name = click.prompt("Enter new name", default=user.name)
        new_email = click.prompt("Enter new email", default=user.email)
        user.name = new_name
        user.email = new_email
        click.echo(f"User {user_id} updated successfully!")
    else:
        click.echo(f"No user found with ID {user_id}.")

# Budget commands
@cli.group()
def budget():
    """Manage budgets"""
    pass

@budget.command()
def add():
    """Add a new budget"""
    name = click.prompt("Enter budget name")
    amount = click.prompt("Enter budget amount", type=float)
    new_budget = Budget(len(budgets) + 1, name, amount)
    budgets.append(new_budget)
    click.echo(f"Budget {name} added successfully!")

@budget.command()
def view():
    """View all budgets"""
    if budgets:
        for budget in budgets:
            click.echo(budget)
    else:
        click.echo("No budgets found.")

@budget.command()
def remove():
    """Remove a budget by ID"""
    budget_id = click.prompt("Enter budget ID to remove", type=int)
    global budgets
    budgets = [b for b in budgets if b.id != budget_id]
    click.echo(f"Budget with ID {budget_id} removed.")

@budget.command()
def update():
    """Update a budget by ID"""
    budget_id = click.prompt("Enter budget ID to update", type=int)
    budget = next((b for b in budgets if b.id == budget_id), None)
    if budget:
        new_name = click.prompt("Enter new name", default=budget.name)
        new_amount = click.prompt("Enter new amount", type=float, default=budget.amount)
        budget.name = new_name
        budget.amount = new_amount
        click.echo(f"Budget {budget_id} updated successfully!")
    else:
        click.echo(f"No budget found with ID {budget_id}.")

# Expense commands
@cli.group()
def expense():
    """Manage expenses"""
    pass

@expense.command()
def add():
    """Add a new expense"""
    name = click.prompt("Enter expense name")
    amount = click.prompt("Enter expense amount", type=float)
    budget_id = click.prompt("Enter associated budget ID", type=int)
    budget = next((b for b in budgets if b.id == budget_id), None)
    if budget:
        new_expense = Expense(len(expenses) + 1, name, amount, budget_id)
        expenses.append(new_expense)
        click.echo(f"Expense {name} added successfully!")
    else:
        click.echo(f"No budget found with ID {budget_id}.")

@expense.command()
def view():
    """View all expenses"""
    if expenses:
        for expense in expenses:
            click.echo(expense)
    else:
        click.echo("No expenses found.")

@expense.command()
def remove():
    """Remove an expense by ID"""
    expense_id = click.prompt("Enter expense ID to remove", type=int)
    global expenses
    expenses = [e for e in expenses if e.id != expense_id]
    click.echo(f"Expense with ID {expense_id} removed.")

@expense.command()
def update():
    """Update an expense by ID"""
    expense_id = click.prompt("Enter expense ID to update", type=int)
    expense = next((e for e in expenses if e.id == expense_id), None)
    if expense:
        new_name = click.prompt("Enter new name", default=expense.name)
        new_amount = click.prompt("Enter new amount", type=float, default=expense.amount)
        expense.name = new_name
        expense.amount = new_amount
        click.echo(f"Expense {expense_id} updated successfully!")
    else:
        click.echo(f"No expense found with ID {expense_id}.")

if __name__ == "__main__":
    cli()