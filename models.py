class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def get_details(self):
        return f"[{self.date}] {self.category.upper()}: ₹{self.amount:.2f} | Note: {self.description}"

    def to_csv_format(self):
        return f"{self.date},{self.category},{self.amount},{self.description}\n"
    