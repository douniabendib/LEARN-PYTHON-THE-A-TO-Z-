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
