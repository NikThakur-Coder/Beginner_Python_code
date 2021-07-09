class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def new_account(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner} \nAccount Balance: {self.balance}'

    def deposit(self, amount):
        print('Deposit accepted!')
        self.balance = self.balance + amount
        return f'Now {self.owner} has {self.balance} in the Account'

    def withdraw(self, amount):
        if self.balance > amount:
            print('Withdrawal Accepted!')
            self.balance = self.balance - amount
            return f'Now {self.owner} has {self.balance} in the Account'
        else:
            return 'Funds Unavailable!'

while True:
    print('To proceed further you need to open an account here')
    decesion = input('Please let us know if You want to open Yes or No: ').lower()
    if decesion == 'yes':
        owner = input('Please enter ur name: ')
        balance = int(input('Please enter your opening balance: '))
        acc1 = Account(owner, balance)
        print(acc1)
        break
    else:
        print("Thanks to visit!")
    break

while decesion == 'yes':
    print('Please let us know if you want to deposit or withdrawal money or want to check balance! ')
    new_decesion = input('Please enter deposit, withdrawal, balance or quit: ')
    if new_decesion == 'deposit':
        amount = int(input('Please enter the deposit amount: '))
        print(acc1.deposit(amount))
    elif new_decesion == 'withdrawal':
        amount = int(input('Please enter the withdrawal amount: '))
        print(acc1.withdraw(amount))
    elif new_decesion == 'balance':
        print(f'Your Account Balance is {acc1.balance} rupees')
    elif new_decesion == 'quit':
        break
