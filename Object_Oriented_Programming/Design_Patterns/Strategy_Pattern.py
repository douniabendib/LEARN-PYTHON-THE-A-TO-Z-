"""
Implement a new BitcoinPayment strategy for our shopping system.

Your task is to:

Create a BitcoinPayment class that implements PaymentStrategy
It should accept a wallet_address in the constructor
The pay method should print exactly: Paying $X using Bitcoin wallet:
 Y where X is the amount and Y is the wallet address
The pay method should return True after printing
Write a main function that:
Creates a shopping cart
Adds a laptop costing $1200 and headphones costing $100 to the cart
Creates a BitcoinPayment with the wallet address "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
Sets this payment strategy on the cart
Calls the checkout method
Follow the same structure as shown in the lesson examples. 
Don't forget to add the conditional if __name__ == "__main__": 
to call your main function
"""
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """Create an abstract strategy interface"""
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    """Implement concrete strategies"""
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card: {self.card_number}")
        return True


class PayPalPayment(PaymentStrategy):
    """Create another payment strategy"""
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Paying ${amount} using Paypal account: {self.email}")
        return True


class ShoppingCart:
    """Create a context class that will use these strategies"""
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        else:
            raise ValueError("No payment strategy set")


class BitcoinPayment(PaymentStrategy):
      """Create a BitcoinPayment class that implements PaymentStrategy"""
      def __init__(self, wallet_address):
          super().__init__()
          self.wallet_address = wallet_address

      def pay(self, amount):
          print(f"Paying ${amount} using Bitcoin wallet: {self.wallet_address}")
          return True


# Create a main function to demonstrate the strategy patterns
def main():
    shopping_cart = ShoppingCart()
    shopping_cart.add_item("laptop", 1200)
    shopping_cart.add_item("headphones", 100)
    wallet = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    shopping_cart.set_payment_strategy(wallet)
    shopping_cart.checkout()


if __name__ == "__main__":
    main()
