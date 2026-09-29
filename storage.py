import os
from models import Expense

# Saves data in the exact same folder as the scripts

script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(script_dir, "expenses_data.txt")

def load_data(expense_list):
    monthly_budget = 0.0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                try:
                    monthly_budget = float(lines[0].strip())
                    for line in lines[1:]:
                        data = line.strip().split(',')
                        if len(data) == 4:
                            expense_list.append(Expense(data[0], data[1], data[2], data[3]))
                except ValueError:
                    pass
    return monthly_budget

def save_data(monthly_budget, expense_list):
    with open(DATA_FILE, "w") as file:
        file.write(f"{monthly_budget}\n")
        for exp in expense_list:
            file.write(exp.to_csv_format())