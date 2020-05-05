from helpers import BankAccount

name = input('Tell us your name: ')
initial_deposit = int(input('How much money would you like to add: '))

bank_account = BankAccount(name)
bank_account.add_deposit(initial_deposit)
#bank_account.make_withdrawal(11)

print(bank_account.__dict__)