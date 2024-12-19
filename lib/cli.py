import click
from helpers import get_connection
from models.User import User
def user():
    pass
@user.command("add")
@click.argument("name")
@click.argument("email")
@click.argument("password")
def add_user(name,email,password):
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