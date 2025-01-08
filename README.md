# Personal Budget Tracker CLI

## Overview

The Personal Budget Tracker is a command-line interface (CLI) application that helps users manage their personal budgets, users, and expenses. This README will guide you through the setup and usage of the application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.6 or higher**
- **SQLite** (comes pre-installed with Python)
- **`pip`** (Python package installer)

## Installation

1. **Clone the Repository**  
   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/kevi799/python-p3-v2-final-project-template
   cd personal-budget-tracker
   ```

# Installation and Usage Guide

### Install Required Packages

Install the necessary Python packages using pip:

```bash
pip install click bcrypt
```

### Initialize the Database

The application requires a SQLite database. Run the following command to initialize the database:

```bash
python -c "budget_tracker.db; init_db()"
```

## Running the CLI

To run the CLI application, execute the following command in your terminal:

```bash
python cli.py user add: python cli.py


```

## Available Commands

Once the CLI is running, you can use the following commands:
start by using the following command first to add view or delete the user,expense or budget

```
python cli.py
```

### User Management

- `user add`: Add a new user
- `user view`: View all users
- `user delete <user_id>`: Delete a user by their ID

### Budget Management

- `budget add`: Add a new budget
- `budget view`: View all budgets
- `budget update <budget_id>`: Update a budget by its ID
- `budget delete <budget_id>`: Delete a budget by its ID

### Expense Management

- `expense add`: Add a new expense
- `expense view`: View all expenses
- `expense update <expense_id>`: Update an expense by its ID
- `expense delete <expense_id>`: Delete an expense by its ID

## Example Usage

### Add a User

```bash
python your_module_name.py user add
```

Follow the prompts to enter the user's name, email, and password.

### View All Users

```bash
python your_module_name.py user view
```

### Add a Budget

```bash
python your_module_name.py budget add
```

### Add an Expense

```bash
python your_module_name.py expense add
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Kevin Mulwa

```

```
