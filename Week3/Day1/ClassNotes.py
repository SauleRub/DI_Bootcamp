# class Dog:
#     def __init__(self, name, color):
#         print("The dog has been initialized")
#         self.name = name
#         self.color = color


# my_dog = Dog('Totti', 'Black')
# laras_dog = Dog("Mizette", 'Brown')

# print(f"{my_dog.name} is {my_dog.color}")
# print(laras_dog.name)


# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)


# Analyse the code below. What will be the output ?
# Explain the goal of the methods
# Create a method that modifies the name of the person
# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36)
# first_person.show_details()

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


SauleAcc = BankAccount(1, 100)
ArikAcc = BankAccount(2, 950000)

SauleAcc.withdraw(100)
ArikAcc.withdraw(2000)

SauleAcc.view_transactions()
ArikAcc.view_transactions()