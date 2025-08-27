class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def addExpense(self, expense):
        self.expenses = expense
        expense.append(self)
ExpenseTracker = ExpenseTracker()
ExpenseTracker.addExpense("Suga")
ExpenseTracker.expenses
