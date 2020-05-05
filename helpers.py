class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def add_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def check_balance(self,amount):
        if(self.balance - amount) < 0:
            print(f'Not enough money, Sorry')
    
    def is_balance_positive(self):
        if self.balance <= 0:
            print(f'You have {self.balance} dollars, and not enough money ')