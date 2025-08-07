# Introduction to Decorators

Decorators are a way to modify or enhance functions and classes without changing their original code. They use the @ symbol.

Here is an example of a simple decorator: 
```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
```
Apply the decorator using @:
```python
@my_decorator
def say_hello():
    print("Hello!")
```
Call the decorated function:
```python
say_hello()
```
Output:
```python
Before function runs
Hello!
After function runs
```
The @my_decorator is equivalent to writing:
```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```
But the @ syntax is much cleaner and easier to read.

Key Point: Decorators wrap around functions to add extra functionality without modifying the original function code.

## Property Decorator

The @property decorator allows you to access methods like attributes, providing a clean way to get and set values.

Here is an example of a class using @property:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```
Create a circle and access properties:
```python
my_circle = Circle(5)
```
Access properties like regular attributes:
```python
print(my_circle.radius)
print(my_circle.area)
#Output:
5
78.53975
```
Notice you don't use parentheses () when accessing properties - they look like attributes but run method code.

Add a setter to allow changing values:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive!")
```
Now you can set the radius like an attribute:
```python
my_circle = Circle(5)
my_circle.radius = 10  # Uses the setter
print(my_circle.radius)  # Uses the getter
#Output:
10
```
Key Point: @property makes methods look like attributes, while @property_name.setter allows you to control how values are assigned.

## Static Method Decorator

The @staticmethod decorator creates methods that don't need self or the class. They work like regular functions but belong to the class.

Here is an example of a class with static methods:
```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
```
Call static methods using the class name:
```python
result = MathHelper.add(5, 3)
print(result)

check = MathHelper.is_even(10)
print(check)
```
You can also call them from an object:
```python
helper = MathHelper()
result2 = helper.add(2, 4)
print(result2)
#Output:

8
True
6
```
Static methods don't access instance or class data:
```python
class Calculator:
    brand = "Python Calc"
    
    def __init__(self, owner):
        self.owner = owner
    
    @staticmethod
    def multiply(x, y):
        # Cannot access self.owner or Calculator.brand
        return x * y
```
Key Point: Use @staticmethod when you need a function that's related to the class but doesn't need access to instance (self) or class data. No self parameter needed.

## Class Method Decorator

The @classmethod decorator creates methods that receive the class itself as the first parameter (cls) instead of an instance (self).

Here is an example of a class with class methods:
```python
class Student:
    school_name = "Python Academy"
    student_count = 0
    
    def __init__(self, name):
        self.name = name
        Student.student_count += 1
    
    @classmethod
    def get_school_info(cls):
        return f"School: {cls.school_name}, Students: {cls.student_count}"
    
    @classmethod
    def create_guest_student(cls):
        return cls("Guest")
```
Call class methods using the class name:
```python
info = Student.get_school_info()
print(info)
```
Create some students:
```python
alice = Student("Alice")
bob = Student("Bob")

updated_info = Student.get_school_info()
print(updated_info)
```
Use class methods as alternative constructors:
```python
guest = Student.create_guest_student()
print(guest.name)
print(Student.get_school_info())
#Output

School: Python Academy, Students: 0
School: Python Academy, Students: 2
Guest
School: Python Academy, Students: 3
```
Class methods can also be called from instances:
```python
alice = Student("Alice")
info_from_instance = alice.get_school_info()
print(info_from_instance)
#Output:

School: Python Academy, Students: 1
```
Key Point: Use @classmethod when you need to access class attributes or create alternative ways to construct objects. The first parameter is cls (the class itself), not self.
