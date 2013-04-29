# bankaccount.py

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdrawal(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def display(self):
        print(self.account_no)
        print(self.balance)
