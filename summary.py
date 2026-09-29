def view_summary(expense_list, monthly_budget):
    print("\n--- Expense Summary ---")
    if not expense_list:
        print("\nNo expenses yet. Add some first!")
        return

    total_spent = 0.0
    category_totals = {"Food": 0, "Transport": 0, "Academics": 0, "Hostel": 0, "Misc": 0}

    print("\nRecent Transactions:")
    for exp in expense_list[-5:]:
        print(exp.get_details())
        
    for exp in expense_list:
        total_spent += exp.amount
        if exp.category in category_totals:
            category_totals[exp.category] += exp.amount

    print("\nCategory Breakdown:")
    for cat, total in category_totals.items():
        if total > 0:
            print(f"{cat.ljust(12)}: ₹{total:.2f}")

    print("-" * 30)
    print(f"Total Spent    : ₹{total_spent:.2f}")
    
    if monthly_budget > 0:
        print(f"Monthly Budget : ₹{monthly_budget:.2f}")
        remaining = monthly_budget - total_spent
        
        if remaining < 0:
            print(f"Status         : BROKE! Over budget by ₹{abs(remaining):.2f}")
        elif remaining < (0.2 * monthly_budget):
            print(f"Status         : Careful, only ₹{remaining:.2f} left.")
        else:
            print(f"Status         : Safe. You still have ₹{remaining:.2f}")
    print("-" * 30)