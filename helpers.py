class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def add_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def check_balance(self,amount):
        return self.balance - amount >= 0
                   
    def is_balance_positive(self):
        return self.balance >= 0
            