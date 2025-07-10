"""
Create a Calculator class that demonstrates your understanding 
of OOP concepts. Your class should:

Have a constructor that initializes a result attribute to 0
Include methods for add, subtract, multiply, and divide that each:
Take a number as an argument
Perform the operation between the current result and the number
Update the result attribute
Return the new result
Include a clear method that resets the result to 0
Include a get_result method that returns the current result
For the divide method, you must handle division by zero by:
Checking if the provided number equals 0
If it is zero, print exactly: "Error: Division by zero"
Leave the result attribute unchanged in this case
Return the unchanged result value
"""
class Calculator:
    def __init__(self):
        # Initialize the result attribute to 0
        self.result = 0
    
        
    def add(self, number):
        # Add the number to result and return the new result
        self.result += number
        return self.result


    def subtract(self, number):
        # Subtract the number from result and return the new result
        self.result -= number
        return self.result
    
    def multiply(self, number):
        # Multiply result by the number and return the new result
        self.result *= number
        return self.result
    

    def divide(self, number):
        # Check if number is 0
        # If it is, print error message and return unchanged result
        # Otherwise, divide result by the number and return the new result
        if number == 0:
            print(f"Error: Division by zero")
        else:
            self.result /= number
        return self.result
    

    def clear(self):
        # Reset result to 0 and return it
        self.result = 0
        return self.result
    

    def get_result(self):
        # Return the current value of result
        return self.result


calc = Calculator()
print(calc.add(5))      # result becomes 5
print(calc.multiply(3))  # result becomes 15
print(calc.subtract(2))  # result becomes 13
print(calc.divide(0))    # prints "Error: Division by zero", result remains 13
print(calc.divide(2))    # result becomes 6.5
print(calc.clear())      # result becomes 0


