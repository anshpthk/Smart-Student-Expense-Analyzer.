import storage
import budget_manager
import summary

def main():
    expense_list = []
    # Load data right when the program starts
    monthly_budget = storage.load_data(expense_list)
    
    while True:
        print("\n" + "="*35)
        print("   STUDENT EXPENSE TRACKER")
        print("="*35)
        print("1. Set/Update Budget")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        print("="*35)
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            monthly_budget = budget_manager.set_budget()
            storage.save_data(monthly_budget, expense_list)
        elif choice == '2':
            budget_manager.add_expense(expense_list, monthly_budget)
        elif choice == '3':
            summary.view_summary(expense_list, monthly_budget)
        elif choice == '4':
            print("\nSaving stuff and exiting... Bye!\n")
            storage.save_data(monthly_budget, expense_list)
            break
        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()