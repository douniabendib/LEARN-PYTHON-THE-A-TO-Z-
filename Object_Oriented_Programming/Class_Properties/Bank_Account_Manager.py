"""
Create a complete BankAccount class that demonstrates object-oriented
programming concepts including class variables, private attributes, 
properties, getters, setters, and methods.

Requirements
1. Create a BankAccount class with:
A class variable interest_rate set to 0.02 (2%)
Private instance attributes for __owner_name and __balance
A constructor that initializes these attributes
2. Implement property getters and setters:
A read-only property owner_name that returns the account owner's name
A property balance with:
A getter that returns the current balance
A setter that validates deposits (rejecting negative amounts)
If validation fails, print: "Balance cannot be negative"
3. Implement methods:
deposit(amount) that:
Adds to the balance if amount is positive
Prints "Deposit amount must be positive" and returns False if amount 
is not positive
Returns True on success
withdraw(amount) that:
Subtracts from the balance if amount is positive and funds are 
sufficient
Prints "Withdrawal amount must be positive" and returns False 
if amount is not positive
Prints "Insufficient funds" and returns False if amount exceeds balance
Returns True on success
apply_interest() that:
Adds interest to the balance based on the class interest rate
Returns the interest amount
display_info() that prints account details in this format:

Account Owner: [owner_name]
Balance: $[balance]
Interest Rate: [interest_rate]%
Output Format Requirements
All validation error messages must be printed exactly as specified
The display_info() method must format the output exactly as shown above
Interest rate should be displayed as a percentage (multiply by 100)
"""
class BankAccount:
    # Class variable for the interest rate
    interest_rate = 0.02

    def __init__(self, owner_name, balance):
        self.__owner_name = owner_name
        self.__balance = balance

    @property
    def owner_name(self):
        """Read-only property for the owner's name."""
        return self.__owner_name

    @property
    def balance(self):
        """Property for the account balance."""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """Setter for balance that rejects negative amounts."""
        if value < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = value

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Deposit amount must be positive")
            return False

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if self.__balance < amount:
            print("Insufficient funds")
            return False
        
        self.__balance -= amount
        return True

    def apply_interest(self):
        """Apply interest to the balance and return the interest amount."""
        interest_amount = self.__balance * BankAccount.interest_rate
        self.__balance += interest_amount
        return interest_amount

    def display_info(self):
        """Display account information."""
        print(f"Account Owner: {self.__owner_name}")
        print(f"Balance: ${self.__balance}")
        print(f"Interest Rate: {BankAccount.interest_rate * 100:.1f}%") 


# Example usage
if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    account.display_info()

    account.deposit(500)
    account.withdraw(200)
    interest_earned = account.apply_interest()
    print(f"Interest earned: ${interest_earned:.2f}")

    account.display_info()
