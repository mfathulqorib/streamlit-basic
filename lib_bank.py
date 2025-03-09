class BankAccount:

    def __init__(self, username, balance = 0):
        try:
            if not isinstance(balance, int):
                raise TypeError("Balance must be an integer.")
            
            self.username = username
            self.balance = balance

        except TypeError as err:
            print(f"error: {err}")


    def deposit(self, amount): 
        self.balance += amount
        print(f"{amount} deposited!")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawed!")

    def check_balance(self):
        print(f"Account: {self.username}, Balance : {self.balance}")

reza_account = BankAccount ("Reza", 1000)
jessy_account = BankAccount ("Jessy", 800)

reza_account.check_balance()
# jessy_account.check_balance()

# reza_account.withdraw(200)
# jessy_account.deposit(350)

# reza_account.check_balance()
# jessy_account.check_balance()
 
