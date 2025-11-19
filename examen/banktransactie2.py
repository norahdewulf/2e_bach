from bankaccount import BankAccount
from examen.banktransacties import accounts_list

class BankTransactie:

    accounts_list = BankAccount(["NL01BANK0123456789","BE68BANK12345678", "NL03BANK1357924680"], [1000.00, 500.00, 1200.50])

    def __init__(self, account_list):
        self.accounts_list = accounts_list
        self.source_account = accounts_list[0]
        self.target_account = accounts_list[1]

    def transfer_funds(self, source_account: str, target_account: str, amount: float, accounts_list: list):
        if (self.source_account not in self.accounts_list) or (self.target_account not in self.accounts_list):
            return "account(s) niet gevonden"
        else:
            if amount < 0:
                return "bedrag moet positief zijn"
            else:
                if self.accounts_list[self.accounts_list.index(self.source_account) + 1] < amount:
                    return "onvoldoende saldo"
                else:
                    self.accounts_list[self.accounts_list.index(self.source_account) + 1] -= amount
                    self.accounts_list[self.accounts_list.index(self.target_account) + 1] += amount
                    return "overboeking geslaagd"

    def new_day(self, accounts_list: list):
        accounts_list.amount_withdrawn_today = 0

bank1 = BankTransactie(accounts_list)
print(bank1.transfer_funds("NL01BANK0123456789", "BE68BANK12345678", 100, ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))
print(bank1.transfer_funds("NL01BANK0123456799", "BE68BANK12345678", 100, ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))
print(bank1.transfer_funds("NL01BANK0123456789", "BE68BANK12345678", 2000, ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))
print(bank1.new_day(BankTransactie(accounts_list)))