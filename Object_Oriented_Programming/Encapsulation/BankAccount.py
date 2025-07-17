class BankAccount:
    """Class to represent a bank account."""
    
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder  # Public attribute
        self.__balance = 0.0  # Private attribute
        self.__account_number = account_number  # Private attribute
        self._transaction_count = 0  # Protected attribute

    def deposit(self, amount):
        """Add to the balance and return the new balance."""
        if amount > 0:
            self.__balance += amount
            self._update_transaction_count()
            return self.get_balance()
        else:
            raise ValueError("Deposit amount must be positive.")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    def _update_transaction_count(self):
        """Increment the transaction count (protected method)."""
        self._transaction_count += 1

    def get_transaction_count(self):
        """Public method to access the transaction count."""
        return self._transaction_count


# Test the BankAccount class
def test_bank_account():
    # Create a bank account
    account = BankAccount("Alice Smith", "123456789")
    
    # Make deposits
    print(f"Initial balance: {account.get_balance()}")
    new_balance = account.deposit(100)
    print(f"Balance after deposit: {new_balance}")
    
    new_balance = account.deposit(50)
    print(f"Balance after another deposit: {new_balance}")
    
    # Access public attribute
    print(f"Account holder: {account.account_holder}")
    
    # Access protected attribute (not recommended)
    print(f"Transaction count (protected): {account._transaction_count}")
    
    # Access transaction count through public method
    print(f"Transaction count (through method): {account.get_transaction_count()}")

    # Attempt to access private attributes (will raise an error)
    try:
        print(account.__balance)  # This will fail
    except AttributeError as e:
        print(f"Error accessing private attribute: {e}")

    try:
        print(account.__account_number)  # This will fail
    except AttributeError as e:
        print(f"Error accessing private attribute: {e}")

# Run the test
test_bank_account()
