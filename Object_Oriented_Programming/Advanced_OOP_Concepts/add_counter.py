def add_counter(cls):
    # Initialize the call_counts dictionary
    cls.call_counts = {"add": 0, "subtract": 0}
    
    # Store original methods
    original_add = cls.add
    original_subtract = cls.subtract
    
    # Define wrapped methods
    def wrapped_add(self, a, b):
        # Increment counter and call original method
        self.call_counts["add"] += 1
        return original_add(self, a, b)  # Call the original method
    def wrapped_subtract(self, a, b):
        # Your code here: Increment counter and call original method
        self.call_counts["subtract"] += 1
        return original_subtract(self, a, b)  # Call the original method

    # Replace original methods with wrapped versions
    cls.add = wrapped_add
    cls.subtract = wrapped_subtract
    
    return cls

@add_counter
class Calculator:
    def __init__(self):
        pass
        
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b

# Test code
calc = Calculator()
print(calc.add(5, 3))
print(calc.add(2, 7))
print(calc.subtract(10, 4))
print(calc.call_counts)  # Should show method call counts
