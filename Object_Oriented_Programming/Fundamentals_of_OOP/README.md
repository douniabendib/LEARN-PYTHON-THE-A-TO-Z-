# Object-Oriented Programming

## Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects rather than functions and logic. In OOP, an object is a collection of data (attributes) and functions (methods) that operate on that data.

Python is an object-oriented language, which means everything in Python is an object - even integers, strings, and functions.

The key concepts in OOP include:

- Classes: Blueprints for creating objects
- Objects: Instances of classes
- Attributes: Data stored inside a class or object
- Methods: Functions defined inside a class

Here's a simple example of defining a class in Python:
```python
# Define a class named 'Person'
class Person:
    pass  # 'pass' is a placeholder that does nothing

# Create an object of the Person class
john = Person()
```
In the next lessons, we'll explore these concepts in depth and learn how to define attributes and methods for our classes.

## Clean Code

Paradigms like object-oriented programming and functional programming are all about making code easier to work with. After all, programmers are just feeble humans. Code that's easy for humans to understand is called "clean code".

Clean Code Does Not:
- Make your programs run faster
- Make your programs function correctly
- Only occur in object-oriented programming

Clean Code Does:
- Make code easier to work with
- Make it easier to find and fix bugs
- Make the development process faster
- Help us retain our sanity

## DRY Code

Another "rule of thumb" for writing maintainable code is "Don't Repeat Yourself" (DRY). It means that, when possible, you should avoid writing the same code in multiple places. Repeating code can be bad because:

- If you need to change it, you have to change it in multiple places
- If you forget to change it in one place, you'll have a bug
- It's more work to write it over and over again

## Classes vs Objects

In Object-Oriented Programming, understanding the difference between classes and objects is fundamental:

* Classes are blueprints or templates that define the structure and behavior for creating objects.

* Objects are instances of classes - concrete entities created from the class blueprint.

Think of a class as a cookie cutter and objects as the cookies made from it:
```python
# Define a class
class Dog:
    # Class attribute (shared by all instances)
```
This creates a simple Dog class with a class attribute species
```python
# Create objects (instances) of the Dog class
dog1 = Dog()
dog2 = Dog()
```
Now we have two different dog objects, but they're empty except for the shared species attribute.
```python
# Add unique attributes to each dog
dog1.name = "Buddy"
dog1.breed = "Golden Retriever"

dog2.name = "Rex"
dog2.breed = "German Shepherd"
```
Each dog now has its own unique attributes.
```python
# Access attributes
print(f"{dog1.name} is a {dog1.breed}")
# Output: Buddy is a Golden Retriever
print(f"{dog2.name} is a {dog2.breed}")
# Output: Rex is a German Shepherd

# Both dogs share the class attribute
print(f"Both dogs are {Dog.species}")
# Output: Both dogs are Canis familiaris
```
The key difference:

- The class (Dog) is the template
- The objects (dog1 and dog2) are specific instances with their own data

    species = "Canis familiaris"

## The self Parameter

In Python, the self parameter is a convention used to refer to the instance of a class within methods. It allows you to access and modify the attributes and call other methods of the current instance.

When you define a method in a class, the first parameter must always refer to the instance itself. By convention, this parameter is named self, though you could technically use any name (but don't - using self is standard practice).
```python
class Dog:
    # Method with self parameter
    def bark(self):
        print("Woof!")
    
    # Method that uses self to access instance attributes
    def describe(self):
        print(f"I am {self.name}, a {self.breed}")
```
Here, self helps the method know which particular dog is barking or being described.

When you create methods, you always include self as the first parameter. However, when you call these methods, you don't explicitly pass a value for self - Python handles this automatically:
```python
# Create a dog object
rex = Dog()
rex.name = "Rex"
rex.breed = "German Shepherd"
```

## Attributes and Methods

In Object-Oriented Programming, classes consist of two main components:

- Attributes: Data or variables that belong to a class or its instances. They represent the state or properties of an object.

- Methods: Functions that belong to a class. They define the behaviors or actions that objects of the class can perform.

Let's explore both concepts:

* Attributes can be:

- Instance attributes: Unique to each object (defined with self)
- Class attributes: Shared across all instances of a class

Let's explore both concepts:
```python
class Student:
    # Class attribute - shared by all instances
    school = "Python High"
    
    def set_details(self, name, age, grade):
        # Instance attributes - unique to each student
        self.name = name
        self.age = age
        self.grade = grade
```

* Methods are functions that are defined within a class and operate on its attributes:
```python
class Student:
    school = "Python High"
    
    def set_details(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    # Method to display student information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    
    # Method with parameters
    def is_passing(self, passing_grade="C"):
        return self.grade <= passing_grade
```
Here's how to use these attributes and methods:
```python
# Create student objects
alice = Student()
bob = Student()

# Set attributes using the method
alice.set_details("Alice", 16, "A")
bob.set_details("Bob", 17, "B")

# Access instance attributes
print(alice.name)
# Output: Alice
print(bob.age)
# Output: 17

# Access class attribute
print(alice.school)
# Output: Python High
print(bob.school)
# Output: Python High

# Call methods
alice.display_info()
# Output: Name: Alice, Age: 16, Grade: A
print(bob.is_passing())
# Output: True
```
## Methods Can Return

If a normal function doesn't return anything, it's typically not a very useful function. In contrast, methods often don't return anything because they can mutate (update) the properties of the object instead. That's exactly what we did in the last assignment.

However, they can return values if you want! They're just functions with access to an object, after all. A common use case is a "getter" method that returns a calculated value based on the properties of the object.

