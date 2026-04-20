import json
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path


# --------- File ----------
TASKS_FILE = Path("mytasktracker.json")




# --------- Load ----------
def load_exp():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []




#--------- Save ----------
def save_exp(data):
    with open(TASKS_FILE, "w") as f:
        json.dump(data, f, indent=4)





#--------- Commands ----------
def add_exp():
    description = input("Enter expense description: ")
    amount = input("Enter expense amount: ")
    date = input("Enter expense date (YYYY-MM-DD): ").strip()

    expense = {
        "description": description,
        "amount": amount,
        "date": date
    }
    data = load_exp()
    data.append(expense)
    save_exp(data)
    print("Expense added successfully!")

def update_exp():
    data = load_exp()
    if not data:
        print("No expenses to update.")
        return

    for i, exp in enumerate(data, start=1):
        print(f"{i}. {exp['description']} - ${exp['amount']} on {exp['date']}")

    exp_num = int(input("Enter the ID of the expense to update: "))
    if 1 <= exp_num <= len(data):
        exp = data[exp_num - 1]
        new_description = input(f"Enter new description (current: {exp['description']}): ") or exp['description']
        new_amount = input(f"Enter new amount (current: {exp['amount']}): ") or exp['amount']

        exp['description'] = new_description
        exp['amount'] = new_amount
        save_exp(data)
        print("Expense updated!")
    else:
        print("Invalid expense ID.")

def delete_exp():
    data = load_exp()
    if not data:
        print("No expenses to delete.")
        return

    for i, exp in enumerate(data, start=1):
        print(f"{i}. {exp['description']} - ${exp['amount']} on {exp['date']}")

    exp_num = int(input("Enter the ID of the expense to delete: "))
    if 1 <= exp_num <= len(data):
        del data[exp_num - 1]
        save_exp(data)
        print("Expense deleted!")
    else:
        print("Invalid expense ID.")

def list_exp():
    data = load_exp()
    if not data:
        print("No expenses recorded.")
        return

    print("Expenses:")
    for i, exp in enumerate(data, start=1):
        print(f"{i}. {exp['description']} - ${exp['amount']} on {exp['date']}")

def summarize_exp():
    data = load_exp()
    if not data:
        print("No expenses recorded.")
        return

    total = sum(float(exp['amount']) for exp in data)
    print(f"You've spent a total of: ${total:.2f}")

def summarize_by_month():
    data = load_exp()
    if not data:
        print("No expenses recorded.")
        return
    monthly_summary = {}
    for exp in data:
        date = datetime.strptime(exp['date'], "%Y-%m-%d")
        month_year = date.strftime("%Y-%m")
        monthly_summary[month_year] = monthly_summary.get(month_year, 0) + float(exp['amount'])

    print("Monthly Expense Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")


def summarize_by_year():
    data = load_exp()
    if not data:
        print("No expenses recorded.")
        return
    yearly_summary = {}
    for exp in data:
        date = datetime.strptime(exp['date'], "%Y-%m-%d")
        year = date.strftime("%Y")
        yearly_summary[year] = yearly_summary.get(year, 0) + float(exp['amount'])

    print("Yearly Expense Summary:")
    for year, total in yearly_summary.items():
        print(f"{year}: ${total:.2f}")





#--------- Main ----------

def main():
    parser = ArgumentParser(description="Expense Tracker")
    parser.add_argument("command", choices=["add", "update", "delete", "list", "summarize", "summarize_month", "summarize_year"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "add":
        add_exp()
    elif args.command == "update":
        update_exp()
    elif args.command == "delete":
        delete_exp()
    elif args.command == "list":
        list_exp()
    elif args.command == "summarize":
        summarize_exp()
    elif args.command == "summarize_month":
        summarize_by_month()
    elif args.command == "summarize_year":
        summarize_by_year()
    else:
        print("Unknown command. Try something else!")

if __name__ == "__main__":
    main()