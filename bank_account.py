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
        if bank_account.check_balance(5) and bank_account.is_balance_positive():
            bank_account.make_withdrawal(5)
            print(f"Your current balance is {bank_account.balance} doll hairs")
        else:
            print('You do not have enough money')
    

    if choice == 2:
        if bank_account.check_balance(3) and bank_account.is_balance_positive():
            bank_account.make_withdrawal(3)
            print(f"Your current balance is {bank_account.balance} doll hairs")
        else:
            print('You do not have enough money')
    

    if choice == 3:
        if bank_account.check_balance(40) and bank_account.is_balance_positive():
            bank_account.make_withdrawal(40)
            print(f"Your current balance is {bank_account.balance} doll hairs")
        else:
            print('You do not have enough money')
    

    if choice == 4:
        amount = int(input('Please enter deposit amount: '))
        bank_account.add_deposit(amount)
        print(f"Your current balance is {bank_account.balance} doll hairs")

exit_status = input("Hit any key to continue or 'q' to quit")
print(bank_account.__dict__)