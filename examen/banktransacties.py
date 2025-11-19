accounts_list = ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]

def transfer_funds(source_account: str, target_account: str, amount: float, accounts_list: list):
    if (source_account not in accounts_list) or (target_account not in accounts_list):
        return "account(s) niet gevonden"
    else:
        if amount < 0:
            return "bedrag moet positief zijn"
        else:
            if accounts_list[accounts_list.index(source_account) + 1] < amount:
                return "onvoldoende saldo"
            else:
                accounts_list[accounts_list.index(source_account) + 1] -= amount
                accounts_list[accounts_list.index(target_account) + 1] += amount
                return "overboeking geslaagd"

def new_day(accounts_list: list):
    self.amount_withdrawn_today = 0

#testen
print(transfer_funds("NL01BANK0123456789", "BE68BANK12345678", 100, ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))
print(transfer_funds("NL01BANK0123456799", "BE68BANK12345678", 100, ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))
print(transfer_funds("NL01BANK0123456789", "BE68BANK12345678", 2000, ["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))
print(new_day(["NL01BANK0123456789", 1000.00, "BE68BANK12345678", 500.00, "NL03BANK1357924680", 1200.50]))

