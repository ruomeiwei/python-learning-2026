class BankAccount:
    """
    A simple bank account, which support deposit and withdraw
    """
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount 
        return self.balance

    def withdraw(self, amount):
        if amount > balance: 
            return 'Balance is not enough'

        self.balance -= amount 
        return self.balance
    def get_balance(self):
        return self.balance


bankaccount = BankAccount(owner='May', balance=10000)

print(bankaccount.deposit(100))

print(bankaccount.deposit(100))