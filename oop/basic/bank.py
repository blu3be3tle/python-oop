class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print (f'broke niqqa, you can\'t withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print (f'bruh ur robbin the empire. you can\'t go beyond {self.max_withdraw}')
        else:
            self.balance -= amount  
            print(f'here\'s your ${amount}, pal')
            print(f'your available balance is ${self.get_balance()}')

brac = Bank(15000)
brac.withdraw(220)