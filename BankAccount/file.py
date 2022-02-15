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
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.account_balance)
    
account1 = BankAccount(.07,2000)
account2 = BankAccount(.04,5000)
print(account1.account_balance)
print(account2.account_balance)

account1.make_deposit(200).make_deposit(600).make_deposit(900).make_withdrawal(550).yield_interest().display_account_info()
account2.make_deposit(300).make_deposit(1179).make_withdrawal(200).make_withdrawal(100).make_withdrawal(200).make_withdrawal(90).yield_interest().display_account_info()

BankAccount.print_all_accounts()