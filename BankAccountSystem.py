
#OOP Mini Project — Bank Account System

# This project ties together everything you've learned in OOP so far:
#
# - Classes & Objects
# - Attributes and Methods
# - Constructors (_init_)
# - Custom behaviors
#
# ✅ Project: Simple Bank Account
#
# We’ll create a class that mimics a real-world bank account where you can:
#
# - Deposit money
# - Withdraw money
# - Check your balance
#
# 🧱 Step-by-step Code:


class BankAccount:
    def __init__(self, accountName, balance=0):
        self.accountName = accountName
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You have deplosited ₹{amount} and your new Balance is: {self.balance}')
        else:
            print(f'Deposit Amount Should be positive ₹{amount}')

    def withDraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'You have withdraw ₹{amount} and your new Balance is: {self.balance}')
        else:
            print(f'Invalid Amount and Insufficient Balance ₹{amount}')

    def checkbalance(self):
        print(f"{self.accountName}, your balance is ₹{self.balance}")



b1 = BankAccount('Jitendra', 100000000000000)
b1.checkbalance()
b1.deposit(200000000)
b1.checkbalance()
b1.withDraw(100000)
b1.checkbalance()
