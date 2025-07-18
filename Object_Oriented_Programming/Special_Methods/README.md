# Magic Methods Introduction

Magic methods (also called dunder methods for "double underscore") are special methods in Python that have double underscores at the beginning and end of their names. These methods are called automatically by Python in response to certain operations or actions.

Magic methods allow you to define how objects of your class behave in various situations, such as when they're converted to strings, compared with other objects, or used with operators.

Here's a simple example showing a class with a magic method:
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # This magic method defines what happens when str() is called on an instance
    def __str__(self):
        return f"{self.title} by {self.author}"

# Creating an instance
my_book = Book("Python Programming", "John Smith", 350)

# When we print the object, __str__ is automatically called
print(my_book)  # Output: Python Programming by John Smith
```
Some common magic methods include:

- __init__: Constructor method, called when an object is created
- __str__: Defines the string representation when str() is called
- __repr__: Defines the string representation when repr() is called
- __len__: Called when the len() function is used on the object
- __add__: Called when the + operator is used
Magic methods make your classes more Pythonic by allowing them to work with built-in functions and operators, providing a more intuitive interface for users of your class.
