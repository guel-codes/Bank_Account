class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def add_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def check_balance(self,amount):
        if (self.balance - amount) < 0:
            print(f'Not enough money, Sorry')
    

bank_account = BankAccount('Miguel')
bank_account.add_deposit(10)
bank_account.make_withdrawal(11)
print(bank_account.__dict__)  

