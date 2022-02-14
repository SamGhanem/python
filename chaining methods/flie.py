class User:
    def __init__(self,username, email):
        self.username = username
        self.email = email
        self.account_balance = 10000
    
    def make_withdrawal(self, amount):
        if (self.account_balance - amount) >= 0:
            self.account_balance -= amount
            print(self.account_balance)
        else:
            print("YOU DONT HAVE THE MONEY!!!!!")
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def transfer_money(self,amount,user):
        if (self.account_balance - amount) >= 0:
            self.account_balance -= amount
            user.account_balance += amount
            print(self.username,self.account_balance)
            print(user.username,user.account_balance)
            print(self.username,"Sent", user.username,"$", amount)
        else:
            print("YOU DONT HAVE THE MONEY!!!!!")
        return self
    
    def display_user_balance(self):
        print(f"User: {self.username}, Balance: {self.account_balance}")
        return self


sam = User("Sam G","Sam.g@gmail.com")
ellie = User("Ellie C","Ellie.c@gmail.com")
max = User("Max B","Max.b@gmail.com")

print("Sam Account:",sam.account_balance)
print("Ellie's Account:",ellie.account_balance)
print("Max's  Account:",max.account_balance)
print(sam.username,sam.email,sam.account_balance)
print(ellie.username,ellie.email,ellie.account_balance)
print(max.username,max.email,max.account_balance)

sam.make_deposit(3000).make_withdrawal(100).make_withdrawal(75).make_withdrawal(90).display_user_balance()

print("***************")

ellie.make_deposit(3000).make_deposit(300).make_deposit(300).make_withdrawal(200).display_user_balance()

print("***************")

max.make_deposit(3000).make_deposit(300).make_withdrawal(100).make_withdrawal(6000).display_user_balance()

print("***************")

# sam.transfer_money(200,ellie)
# sam.display_user_balance
# print(sam.account_balance)
# print("Ellie's Account:",ellie.account_balance)
sam.transfer_money(50,ellie).display_user_balance()
max.display_user_balance()
ellie.display_user_balance()