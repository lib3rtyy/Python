from datetime import date
import json

def add_expense(today_date, expenses, description, amount):
    expenses.append({"date":str(today_date),"description":description,"amount":amount})
    print(f"Expense added: {description}, Amount:{amount} on '{today_date}'")

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget,expenses):
    return budget - get_total_expenses(expenses)


def show_budget_details(report_date, budget, expenses):
    print(f"\nBudget Report for {report_date}")
    print("----------------------------")
    print(f"Current Budget: {budget} \n")
    print("Expenses:")
    print("Date       | Description             | Amount")
    print("---------------------------------------------")
    for expense in expenses:
        print(f"{expense['date']} | {expense['description']:<23} | ${expense['amount']:.2f} ")
    print("\n")
    print(f"Total Spent: {get_total_expenses(expenses):.2f}")
    print(f"Remaining Budget: {get_balance(budget,expenses):.2f}")

def load_budget_data(filepath):
    try:
        with open(filepath,'r') as file:
            data =json.load(file)
            return data.get("initial_budget", 0), data.get("expenses", [])
    except (FileNotFoundError,json.JSONDecodeError):
        return 0 , []

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Budget Tracker")
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("Enter your initial budget:"))
    budget = initial_budget

    while True:
        print("\nSelect a procedure:\n")
        print("\n 1. Add to expenses\n")
        print("\n 2. Show budget details\n")
        print("\n 3. Exit\n")
        choice = input("Enter 1,2 or 3:")

        if choice == "1":
            description = input("Enter expenses description : ")
        
            while True:
                try:
                    amount = float(input("Enter the amount of expenses: "))
                    break
                except ValueError:
                    print("Invalid imput. Please enter a numeric value for the amount!")

            today_date = date.today()
            add_expense(today_date, expenses, description, amount)

        elif choice == "2":
            report_date = date.today()
            show_budget_details(report_date, budget, expenses)

        elif choice == "3":
            save_budget_details(filepath, initial_budget,expenses)
            print("You are about to exit the Budget Tracker! ")
            answer = input("Are you sure Yes or No (Y/N): ").upper()
            if answer == "Y" or answer == "":
                break
            else:
                continue
        else:
            print("Invalid, please select a valid procedure.")


if __name__ == "__main__":
    main()
