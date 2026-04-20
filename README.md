# 💸 Expense Tracker CLI

A simple command-line expense tracker to help you manage and monitor your personal finances. Built with Python, it stores your expenses locally in a JSON file.

> 📌 Project based on: [roadmap.sh/projects/expense-tracker](https://roadmap.sh/projects/expense-tracker)

---

## Features

- Add a new expense with a description and amount
- Update an existing expense
- Delete an expense
- List all recorded expenses
- Summarize total expenses
- Summarize expenses by month
- Summarize expenses by year

---

## Requirements

- Python 3.x
- No external dependencies — uses only the Python standard library

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Run the tracker

```bash
python expense_tracker.py <command>
```

---

## Usage

### Add an expense

```bash
python expense_tracker.py add
```
You'll be prompted to enter:
- Description
- Amount
- Date (YYYY-MM-DD)

### Update an expense

```bash
python expense_tracker.py update
```

### Delete an expense

```bash
python expense_tracker.py delete
```

### List all expenses

```bash
python expense_tracker.py list
```

**Example output:**
```
Expenses:
1. Lunch - $20.00 on 2024-08-06
2. Dinner - $10.00 on 2024-08-06
```

### Summarize total expenses

```bash
python expense_tracker.py summarize
```

**Example output:**
```
You've spent a total of: $30.00
```

### Summarize by month

```bash
python expense_tracker.py summarize_month
```

**Example output:**
```
Monthly Expense Summary:
2024-08: $30.00
```

### Summarize by year

```bash
python expense_tracker.py summarize_year
```

**Example output:**
```
Yearly Expense Summary:
2024: $30.00
```

---

## Data Storage

All expenses are saved locally in a `mytasktracker.json` file in the same directory. The file is created automatically on first use.

Example structure:
```json
[
    {
        "description": "Lunch",
        "amount": "20",
        "date": "2024-08-06"
    }
]
```

---

## Project Structure

```
.
├── expense_tracker.py     # Main application file
├── mytasktracker.json     # Auto-generated data file
└── README.md
```

---

## Possible Improvements

- Add expense categories and filter by category
- Set monthly budgets with overspending warnings
- Export expenses to a CSV file
- Accept arguments directly from the command line (e.g. `--description`, `--amount`) instead of interactive prompts

---

## License

This project is open source and free to use.
