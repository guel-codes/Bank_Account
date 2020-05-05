class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def add_deposit(self, amount):
        self.balance += amount

bank_account = BankAccount('Miguel')
bank_account.add_deposit(10)
print(bank_account.__dict__)  

