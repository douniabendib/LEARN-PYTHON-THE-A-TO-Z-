# Encapsulation

Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.

## Public, Protected, Private Mem

In Python, encapsulation involves controlling access to class attributes and methods. There are three levels of access modifiers:

* Public Members are accessible from anywhere. 
They have no special prefix:
```python
self.name = name        # Public attribute
def display_info(self): # Public method
```
* Protected Members should only be accessed within the class and its subclasses. 
They use a single underscore prefix:
```python
self._age = age         # Protected attribute
def _calculate(self):   # Protected method
```
* Private Members should only be accessed within the class itself. 
They use a double underscore prefix:
```oython
self.__id = id          # Private attribute
def __validate(self):   # Private method
```
Python's privacy mechanisms are conventions, not strict enforcement. Private attributes are name-mangled (renamed to _ClassName__attribute), making them harder but not impossible to access.

## Access Modifiers

Access modifiers in Python help control the visibility and accessibility of class attributes and methods. Unlike some languages, Python uses naming conventions rather than keywords for access control.

Here's how access modifiers work in practice:

* No modifier (Public) - Accessible from anywhere:
```python
class Person:
    def __init__(self):
        self.name = "Coddy"      # Public attribute
        
    def greet(self):             # Public method
        return f"Hello, I'm {self.name}"
```
* Single underscore (Protected) - Should only be accessed within the class and its subclasses:
```python
class Employee:
    def __init__(self):
        self._salary = 50000     # Protected attribute
    
    def _calculate_bonus(self):  # Protected method
        return self._salary * 0.1
```
* Double underscore (Private) - Should only be accessed within the class itself:
```python
class User:
    def __init__(self):
        self.__password = "secure123"   # Private attribute
        
    def __encrypt(self, data):          # Private method
        return f"Encrypted: {data}"
        
    def verify(self, input_password):
        # Private members can be accessed inside the class
        return input_password == self.__password
```
These access modifiers help establish boundaries within your code, making it easier to:

- Prevent accidental modification of important data
- Hide implementation details
- Create a clean public interface for classes
