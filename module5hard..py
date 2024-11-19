# class User:
#
#     def nickname(self, user_name, string):
#         self.user_name = user_name
#         self.string = str(string)
#
#     def password(self, hasher, number):
#         self.hasher = hash(hasher)
#         self.nuuumber = number
#
#     def age(self, user_age, inter):
#         self.user_age = user_age
#         self.inter = int(inter)
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else: self.balance -= amount


account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.balance)