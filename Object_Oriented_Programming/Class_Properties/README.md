# Class Properties

## Instance vs Class Variables

In Python classes, there are two main types of variables (attributes):

Class Variables belong to the class itself and are shared by all instances. They're defined within the class but outside any methods.

Instance Variables belong to individual objects (instances) and can have different values for each object. They're typically defined in the __init__ method using self.

Here's how they differ:
```python
class Student:
    # Class variable - shared by all instances
    school = "Python High School"
    
    def __init__(self, name, grade):
        # Instance variables - unique to each student
        self.name = name
        self.grade = grade
```
Let's see them in action:
```python
# Create student objects
alice = Student("Alice", "A")
bob = Student("Bob", "B")

# Access instance variables (different for each student)
print(alice.name)
# Output: Alice
print(bob.name)
# Output: Bob

# Access class variable (same for all students)
print(alice.school)
# Output: Python High School
print(bob.school)
# Output: Python High School
print(Student.school)
# Output: Python High School

# If we change the class variable
Student.school = "Python Academy"
print(alice.school)
# Output: Python Academy
print(bob.school)
# Output: Python Academy
```
Key differences:

- Class variables are shared among all instances
- Instance variables are unique to each instance
- Class variables are defined once, instance variables for each object

## Property Decorators

Property decorators in Python allow you to define methods that behave like attributes. They provide a way to implement getters, setters, and deleters for class attributes, enabling controlled access to your data.

The main property decorator is @property, which turns a method into a "getter" for a read-only attribute:
```python
class Person:
   def __init__(self, name, age):
       self._name = name
       self._age = age
   
   @property
   def age(self):
       return self._age
```
With this code, age can be accessed like an attribute, but it's actually calling the getter method:
```python
person = Person("Alice", 30)
print(person.age)
# Calls the age() method, returns 30
```
To allow setting values, add a setter method using the @attribute.setter decorator:
```python
@age.setter
def age(self, value):
    if value < 0:
        raise ValueError("Age cannot be negative")
    self._age = value
```
Now you can also set the age, with validation included:
```python
person.age = 31     # Calls the age setter method
print(person.age)   # Output: 31

# This would raise an error:
# person.age = -5   # ValueError: Age cannot be negative
```
Properties are valuable for:

- Data validation
- Computing values on-the-fly
- Encapsulating internal data structures

## Private Attributes

In Python, there's a convention for indicating that an attribute should be treated as private (not accessed directly from outside the class). We prefix the attribute name with a single underscore _ or double underscore __.

Single underscore _attribute: Indicates the attribute is intended for internal use. This is a convention, not a strict rule - the attribute can still be accessed directly.
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        # Convention: "private" attribute
        self._age = age
        # Convention: "private" attribute
```
Double underscore __attribute: Triggers name mangling - Python renames the attribute to make it harder to access directly from outside the class.
```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        # Will be "mangled" to _Person__name
        self.__age = age
        # Will be "mangled" to _Person__age
```
To access private attributes properly, you should create public methods or properties:
```python
def get_name(self):
    return self.__name
    
def set_age(self, age):
    if age >= 0:
        self.__age = age
```
While you can still access double-underscore attributes, it requires knowing the mangled name:

```python
coddy = User("Coddy", 25)
# Direct access (discouraged):
print(coddy._User__name)
# Output: Coddy
```

Private attributes help with:

- Encapsulation (hiding internal details)
- Preventing accidental modification
- Adding validation when values are changed
