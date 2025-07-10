"""
Create a BankAccount class with:

A class variable interest_rate set to 0.02 (2%)
Instance variables for account_holder and balance set 
in the constructor
A display_info method that prints the account information 
in this exact format:

Account: [account_holder]
Balance: $[balance]
Interest Rate: [interest_rate]%
Then:

Create two accounts with these exact details:
account1: holder "Alice Smith" with $1000 balance
account2: holder "Bob Jones" with $2000 balance
Call display_info() for both accounts
Change the class variable interest_rate to 0.03 (3%)
Print the text "After interest rate change:"
Call display_info() for both accounts again to show they both 
have the new interest rate.
"""
class BankAccount:
    # Add class variable here
    interest_rate = 2.0
    # Add __init__ method
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    # Add display_info method
    def display_info(self):
        print(f"Account: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")
        print()

# Create two accounts
account1 = BankAccount("Alice Smith", 1000)
account2 = BankAccount("Bob Jones", 2000)
# Display information for both accounts
account1.display_info()
account2.display_info()
# Modify the interest rate and show it affects all accounts
BankAccount.interest_rate = 3.0
print("After interest rate change:")
account1.display_info()
account2.display_info()
