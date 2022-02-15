class BankAccount:
    
    all_accounts = []
    
    def __init__(self, int_rate = 0, account_balance = 0):
        self.account_balance = account_balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        
    def make_withdrawal(self, amount):
        if (self.account_balance - amount) >= 0:
            self.account_balance -= amount
            print(self.account_balance)
        else:
            self.account_balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def yield_interest(self):
        if self.account_balance >= 0:
            self.account_balance += (self.int_rate * self.account_balance)
        return self
    
    def display_account_info(self):
        print(f" Balance: ${self.account_balance}")
        return f" Balance: ${self.account_balance}"
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.account_balance)
    
class User:
    
    def __init__(self,name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.25,1000),
            "savings" : BankAccount(.08,8000)}
        
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    
    def transfer_money(self,user,amount):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self 
    


sam = User("Sam G")
# sam.account['checking'].display_account_info()
# sam.account['savings'].display_account_info()
sam.display_user_balance()

sam.account['checking'].make_deposit(5097).display_account_info()
sam.account['savings'].make_deposit(2000).display_account_info()

sam.display_user_balance()
