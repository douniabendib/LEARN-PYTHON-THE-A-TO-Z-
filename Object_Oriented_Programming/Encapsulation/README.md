# Encapsulation

Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.

## Public, Protected, Private Mem

In Python, encapsulation involves controlling access to class attributes and methods. There are three levels of access modifiers:

Public Members are accessible from anywhere. They have no special prefix:
```python
self.name = name        # Public attribute
def display_info(self): # Public method
```
Protected Members should only be accessed within the class and its subclasses. They use a single underscore prefix:
```python
self._age = age         # Protected attribute
def _calculate(self):   # Protected method
```
Private Members should only be accessed within the class itself. They use a double underscore prefix:
```oython
self.__id = id          # Private attribute
def __validate(self):   # Private method
```
Python's privacy mechanisms are conventions, not strict enforcement. Private attributes are name-mangled (renamed to _ClassName__attribute), making them harder but not impossible to access.
