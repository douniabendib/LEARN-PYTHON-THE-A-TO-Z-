class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __mul__(self, scalar):
        return Money(self.amount * scalar, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"
        
# Test code - 
def test_money():
    try:
        # Test initialization and string representation
        m1 = Money(10.0, "USD")
        assert str(m1) == "10.00 USD", f"__str__ method failed, got {str(m1)}"
        
        # Test addition
        m2 = Money(20.0, "USD")
        m3 = m1 + m2
        assert str(m3) == "30.00 USD", f"Addition failed, got {str(m3)}"
        
        # Test different currency addition
        m4 = Money(20.0, "EUR")
        try:
            m5 = m1 + m4
            assert False, "Adding different currencies should raise an error"
        except ValueError as e:
            assert str(e) == "Cannot add different currencies", f"Wrong error message: {str(e)}"
        
        # Test multiplication
        m6 = m1 * 3
        assert str(m6) == "30.00 USD", f"Multiplication failed, got {str(m6)}"
        
        # Test equality
        assert m1 == Money(10.0, "USD"), "Equality test failed"
        assert m1 != m2, "Inequality test failed"
        
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

test_money()
