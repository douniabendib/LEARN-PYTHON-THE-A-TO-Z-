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

## Operator Overloading
Operator Overloading

Operator overloading allows your classes to work with Python's built-in operators (+, -, *, etc.) by implementing special magic methods. Each operator corresponds to a specific method:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Using the operators
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)
# Output: Vector(7, 10)
print(v1 * 3)
# Output: Vector(6, 9)
```
Common operator methods include:

__add__ (+), __sub__ (-), __mul__ (*), __truediv__ (/)
__eq__ (==), __lt__ (<), __gt__ (>)

## Container Magic Methods

Container magic methods allow your classes to behave like built-in container types (lists, dictionaries, etc.). These methods enable operations such as indexing, length checking, and iteration on your custom objects.

Key container magic methods include:
```python
class CustomList:
    def __init__(self, items):
        self.items = items
    
    # Makes len(obj) work
    def __len__(self):
        return len(self.items)
    
    # Makes obj[index] work for retrieval
    def __getitem__(self, index):
        return self.items[index]
    
    # Makes obj[index] = value work for assignment
    def __setitem__(self, index, value):
        self.items[index] = value
    
    # Makes iteration work (for item in obj)
    def __iter__(self):
        return iter(self.items)
    
    # Makes 'in' operator work (item in obj)
    def __contains__(self, item):
        return item in self.items

# Usage example
my_list = CustomList([1, 2, 3, 4])
print(len(my_list))         # Output: 4
print(my_list[2])           # Output: 3
my_list[1] = 10
print(my_list[1])           # Output: 10
print(3 in my_list)         # Output: True

# Iterating works too
for item in my_list:
    print(item)
```
These methods make your custom classes feel more like Python's native data structures, providing a more intuitive interface for users.
