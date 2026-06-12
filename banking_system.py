# Banking System - Method Overloading & Overriding

class Transaction:
    def process(self, *args):
        print("Base transaction")

class Deposit(Transaction):
    def process(self, amount):
        print(f"Deposited UGX {amount:,.0f}")

class Withdrawal(Transaction):
    def process(self, amount):
        print(f"Withdrew UGX {amount:,.0f}")

class Transfer(Transaction):
    def process(self, amount, recipient):
        print(f"Transferred UGX {amount:,.0f} to {recipient}")

name = input("Employer name: ")

d = Deposit()
d.process(500000)

w = Withdrawal()
w.process(200000)

t = Transfer()
t.process(150000, "Supplier A")
