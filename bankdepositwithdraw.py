class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.max_withdraw = 50000
        self.min_withdraw = 500
        self.minimum_balance = 500

    def deposit(self, amount):
        self.balance+=amount
    
    def get_balance(self):
        return f'Your current balance is: {self.balance}'

    def withdraw(self, amount):
        if amount>self.max_withdraw:
            return f"You are crossed the amount of max withdraw: {self.max_withdraw}"
        elif amount<self.min_withdraw:
            return f'You can not withdraw: {amount}\nBecause, minimum withdraw is: {self.min_withdraw}'
        elif amount>self.balance:
            return f'You can not withdraw: {amount}\nBecause, Your balance is: {self.balance}'
        else:
            self.balance-=amount
            return f'Here is your money: {amount}'


my_bank = Bank(0)
my_bank.deposit(10000)
reply = my_bank.get_balance()
print(reply)
reply = my_bank.withdraw(500)
print(reply)
reply = my_bank.get_balance()
print(reply)
    