from helpers import BankAccount

name = input('Tell us your name: ')
initial_deposit = int(input('How much money would you like to add: '))

bank_account = BankAccount(name)
bank_account.add_deposit(initial_deposit)


exit_status = ''
while exit_status.lower() != 'q':
    print("""
    Please choose an item:

    1. Apples: $5
    2. Oat Milk: $3
    3. Crab Legs: $40
    4.Deposit more funds
    """ )

    choice = int(input())
    
    if choice == 1:
        bank_account.make_withdrawal(5)
        print(f"Your current balance is{bank_account.balance}")
        
    exit_status = input("Hit any key to continue or 'q' to quit")

print(bank_account.__dict__)