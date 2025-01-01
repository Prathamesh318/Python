class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, customer_name, initial_balance=0):
        self.accounts[account_number] = {"name": customer_name, "balance": initial_balance}
        print(f"Added account for {customer_name} with initial balance {initial_balance}.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"Deposited {amount} to account {account_number}.")
        else:
            print(f"Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Withdrew {amount} from account {account_number}.")
            else:
                print("Insufficient balance.")
        else:
            print(f"Account {account_number} not found.")

    def display_account(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number}: {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} not found.")

# Example Usage
bank = Bank()
bank.add_account(101, "Alice", 500)
bank.deposit(101, 200)
bank.withdraw(101, 100)
bank.display_account(101)
