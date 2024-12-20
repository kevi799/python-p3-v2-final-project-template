# Personal Budget Tracker CLI

## Overview

The Personal Budget Tracker is a command-line interface (CLI) application that helps users manage their personal budgets, users, and expenses. This README will guide you through the setup and usage of the application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.6 or higher
- SQLite (comes pre-installed with Python)
- `pip` (Python package installer)

## Installation

1. **Clone the Repository**  
   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/yourusername/personal-budget-tracker.git
   cd personal-budget-tracker
   ```

2. **Install Required Packages**  
   Install the necessary Python packages using `pip`:

   ```bash
   pip install click bcrypt
   ```

3. **Initialize the Database**  
   The application requires a SQLite database. Run the following command to initialize the database:
   ```bash
   python -c "from your_module_name import init_db; init_db()"
   ```
   Replace `your_module_name` with the name of the Python file where the `init_db` function is defined.

## Running the CLI

To run the CLI application, execute the following command in your terminal:

```bash
python your_module_name.py
```

Replace `your_module_name.py` with the name of your main Python file containing the CLI code.

### Available Commands

Once the CLI is running, you can use the following commands:

- **User Management**

  - `user add` - Add a new user
  - `user view` - View all users
  - `user delete <user_id>` - Delete a user by their ID

- **Budget Management**

  - `budget add` - Add a new budget
  - `budget view` - View all budgets
  - `budget delete <budget_id>` - Delete a budget by its ID

- **Expense Management**
  - `expense add` - Add a new expense
  - `expense view` - View all expenses

### Example Usage

1. **Add a User**

   ```bash
   python your_module_name.py user add
   ```

   Follow the prompts to enter the user's name, email, and password.

2. **View All Users**

   ```bash
   python your_module_name.py user view
   ```

3. **Add a Budget**

   ```bash
   python your_module_name.py budget add
   ```

4. **Add an Expense**
   ```bash
   python your_module_name.py expense add
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Kevin Mulwa**
