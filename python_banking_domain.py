# #hand_On Code- python getter & setter method to access ,modify the private attributes in banking domain

class hdfc_bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be negetive")

    def deposit_money(self,amount):
        if amount >= 0:
            self.set_balance(self.__balance + amount)
        else:
            print("Error: Deposit money can't be negative")

    def withdraw_money(self,amount):
        if 0 < amount <= self.get_balance():
            self.set_balance(self.__balance - amount)
        else:
            print("Error: Its an Invalid amount or Insufficient Balance")


account = hdfc_bank_account("457788", 15000)
print(account.get_balance())

account.deposit_money(2000)
print(account.get_balance())

account.withdraw_money(16000)
print(account.get_balance())

account.withdraw_money(1500)
account.set_balance(-200)

# __ double underscore makes the balance attribute private. it cannot be accesses or modified directly outside of the class.
# Gettter methos(get_balance):
# this method retrives the value of the private __balance attribute.
# it allows controlles access to the private attribute without exposing it directly
# Setter method(set_balance): this method sets or modifies the value of __balance attribute.
# it incli


