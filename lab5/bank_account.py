class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Saldo nie moze byc ujemne")
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if type(amount) not in (int, float):
            raise ValueError("Kwota musi byc liczba")
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Kwota wplaty musi byc wieksza od zera")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if type(amount) not in (int, float):
            raise ValueError("Kwota musi byc liczba")
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Kwota wyplaty musi byc wieksza od zera")
        if amount > self.balance:
            raise ValueError("Za malo srodkow na koncie")
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance
