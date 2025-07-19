"""Create three mixins for a simple e-commerce system:

PrintableMixin: Adds a print_details() method that returns a formatted string with an object's attributes.
This method should return a string in the format: "Product: {name}, Price: ${price}"
DiscountMixin: Adds an apply_discount(percent) method that calculates a discounted price.
This method should return the price after applying the percent discount
Formula: price - (price * percent / 100)
ShippableMixin: Adds the following methods:
set_weight(weight): Stores the weight attribute
calculate_shipping(): Calculates shipping cost at $0.50 per pound
Formula: weight * 0.5
Then, create:

A Product class that:
Inherits from PrintableMixin and DiscountMixin
Has an __init__ method accepting name and price parameters and setting them as attributes
A PhysicalProduct class that:
Extends Product and also inherits from ShippableMixin
Doesn't need to override any methods
A DigitalProduct class that:
Extends Product
Overrides the apply_discount method with a special fixed 10% discount
"""
# Implement the mixins
class PrintableMixin:
    def print_details(self):
        return f"Product: {self.name}, Price: ${self.price}"

class DiscountMixin:
    def apply_discount(self, percent): 
        return self.price - (self.price * percent / 100)

class ShippableMixin:
    def set_weight(self, weight):
        self.weight = weight
    
    def calculate_shipping(self):
        return self.weight * 0.5

# Implement the product classes
class Product(PrintableMixin, DiscountMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    

class PhysicalProduct(Product, ShippableMixin):
    pass

class DigitalProduct(Product):
    def apply_discount(self, percent):
        return (self.price - (self.price * 10 / 100))

# Test code - 
def test_mixins():
    try:
        # Test PrintableMixin
        p = Product("Laptop", 1000)
        assert p.print_details() == "Product: Laptop, Price: $1000", f"Print details failed: {p.print_details()}"
        
        # Test DiscountMixin
        assert p.apply_discount(10) == 900, f"Discount calculation failed: {p.apply_discount(10)}"
        
        # Test PhysicalProduct with ShippableMixin
        physical = PhysicalProduct("Desk", 500)
        physical.set_weight(30)
        assert physical.calculate_shipping() == 15, f"Shipping calculation failed: {physical.calculate_shipping()}"
        
        # Test DigitalProduct with special discount
        digital = DigitalProduct("Software", 200)
        assert digital.apply_discount(10) == 180, f"Digital discount failed: {digital.apply_discount(10)}"
        
        print("All tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")

test_mixins()
