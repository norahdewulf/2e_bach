class BankAccount:
    def __init__(self, account_number, balance = 0.0, daily_limit = 1000.0):
        if account_number.startswith("NL") or account_number.startswith("BE"):
            self.account_number = account_number
        else:
            self.account_number = 0
            print("error")
        self.balance = balance
        self.daily_limit = daily_limit
        self.amount_withdrawn_today = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            return "error"

    def withdraw(self, amount):
        if (amount > 0) and (self.amount_withdrawn_today <= self.daily_limit) and (amount <= self.balance):
            self.balance -= amount
            self.amount_withdrawn_today += amount
            return "inorde!"
        else:
            return "error"

    def reset_daily_limit(self):
        self.amount_withdrawn_today = 0.0

    def __str__(self):
        return f"{self.account_number}, {self.balance}, {self.daily_limit}"