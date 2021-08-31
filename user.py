class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        self.account_balance = self.account_balance + self.make_deposit - self.make_withdrawal

    def transfer_money(self, other_user, amount):
        self.other_user = other_user
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount

bankUser1 = User("John Elway", "JohnE@denverbroncos.com")
bankUser2 = User("Peyton Manning", "PeytonM@denverbroncos.com")
bankUser3 = User("Karl Meklenburg", "KarlM@denverbroncos.com")

bankUser1.make_deposit(100)
bankUser1.make_deposit(100)
bankUser1.make_deposit(100)
bankUser1.make_withdrawal(50)

print(bankUser1.name)
print(bankUser1.account_balance)

bankUser2.make_deposit(100)
bankUser2.make_deposit(100)
bankUser2.make_withdrawal(50)
bankUser2.make_withdrawal(50)

print(bankUser2.name)
print(bankUser2.account_balance)

bankUser3.make_deposit(200)
bankUser3.make_withdrawal(50)
bankUser3.make_withdrawal(50)
bankUser3.make_withdrawal(50)

print(bankUser3.name)
print(bankUser3.account_balance)

bankUser1.transfer_money(bankUser3, 100)
print(bankUser1.name)
print(bankUser1.account_balance)
print(bankUser3.name)
print(bankUser3.account_balance)