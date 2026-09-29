from datetime import datetime
from models import Expense
import storage

def set_budget():
    print("\n--- Set Monthly Budget ---")
    while True:
        try:
            amount = float(input("Enter your total budget for the month (₹): "))
            if amount < 0:
                print("Budget can't be negative bro. Try again.")
                continue
            print(f"\nAwesome, budget set to ₹{amount:.2f}")
            return amount
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def add_expense(expense_list, monthly_budget):
    print("\n--- Add New Expense ---")
    today = datetime.now().strftime("%d-%m-%Y")
    use_today = input(f"Use today's date ({today})? (y/n): ").lower()
    
    date = today if use_today == 'y' else input("Enter date manually (DD-MM-YYYY): ")

    print("\nCategories: 1. Food 2. Transport 3. Academics 4. Hostel 5. Misc")
    while True:
        cat_choice = input("\nSelect a category (1-5): ")
        categories = {'1': "Food", '2': "Transport", '3': "Academics", '4': "Hostel", '5': "Misc"}
        if cat_choice in categories:
            category = categories[cat_choice]
            break
        print("Wrong choice. Pick a number from 1 to 5.")

    while True:
        try:
            amount = float(input("Enter amount spent (₹): "))
            if amount <= 0:
                print("Amount should be more than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    desc = input("Enter a quick description (e.g., 'snacks'): ")
    new_expense = Expense(date, category, amount, desc)
    expense_list.append(new_expense)
    
    # Save immediately after adding
    storage.save_data(monthly_budget, expense_list)
    print("\nExpense recorded successfully!")
    