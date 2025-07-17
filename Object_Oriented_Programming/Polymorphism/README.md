# Polymorphism

## Method Overriding Revisited

Method overriding is a key aspect of polymorphism in object-oriented programming. While we've seen method overriding in the inheritance chapter, let's explore how it enables polymorphic behavior.

Polymorphism means "many forms" and allows objects of different classes to be treated as objects of a common superclass. The most common use of polymorphism is when a parent class reference is used to refer to a child class object.

When methods are overridden in child classes, we can call the same method on different objects and get different behaviors based on the object's actual class:
```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
```
Now we can create a list of different animals and call the same method on each:
```python
animals = [Dog(), Cat(), Cow(), Animal()]

for animal in animals:
    print(animal.speak())

# Output:
# Woof!
# Meow!
# Moo!
# Animal makes a sound
```
This is polymorphism in action - the same method call (speak()) behaves differently depending on the actual object type. We don't need to check the type of each animal or call different methods; we just call speak() and let each class handle it appropriately.

Polymorphism makes code more:

- Flexible: You can add new animal types without changing how they're processed
- Extensible: New behaviors can be added by creating new subclasses
- Clean: You avoid complex if/elif/else chains for different types

## Duck Typing

Duck typing is a concept in programming that focuses on what an object can do, rather than what it is. The name comes from the phrase: "If it walks like a duck and quacks like a duck, then it's probably a duck."

In Python, duck typing means that we don't care about the class type of an object; we only care if it has the methods and properties we need. Unlike traditional inheritance-based polymorphism, duck typing doesn't require a common parent class.

Here's a simple example:
```python
class Duck:
    def swim(self):
        return "Duck swimming"
    
    def quack(self):
        return "Quack!"

class Person:
    def swim(self):
        return "Person swimming"
    
    def quack(self):
        return "Person imitating a duck: Quack!"
```
With duck typing, we can create a function that works with any object that has the required methods:
```python
def make_it_swim_and_quack(duck_like_object):
    print(duck_like_object.swim())
    print(duck_like_object.quack())

# This works for both classes, even though they don't share a parent class
make_it_swim_and_quack(Duck())
make_it_swim_and_quack(Person())
```
Duck typing is powerful because it:

- Provides flexibility
- Reduces dependencies between classes
- Makes code more reusable
- Follows Python's "easier to ask forgiveness than permission" philosophy

## Abstract Classes and Methods

Abstract classes are classes that can't be instantiated directly and are designed to be subclassed. They often contain abstract methods - methods that are declared but don't have an implementation in the abstract class. These methods must be implemented by any concrete (non-abstract) subclass.

Python doesn't have built-in abstract classes, but provides the abc module (Abstract Base Classes) to create them:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return "This is a shape"  # Concrete method
```
A class inheriting from an abstract class must implement all its abstract methods, or it will also be abstract:
```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
```
Abstract classes are useful for:

- Defining interfaces that derived classes must implement
- Providing common functionality while forcing specific implementations
- Creating a clear hierarchy of related classes

## Interface Design

In Python, an interface is a specification for behavior that classes can implement. Unlike some languages, Python doesn't have a formal interface keyword, but we can create interfaces using abstract base classes where all methods are abstract.

A well-designed interface should:

- Define a clear contract for implementing classes
- Be focused on a specific set of related functionality
- Have method names that clearly indicate their purpose

Here's how to create an interface in Python:
```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def resize(self, width, height):
        pass
```
Classes can then implement this interface:
```python
class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        return "Drawing a circle"
    
    def resize(self, width, height):
        self.radius = min(width, height) / 2
        return f"Resized circle to radius {self.radius}"
```
Interfaces help with:

- Creating plug-and-play components
- Ensuring all implementations provide required functionality
- Making code more maintainable and testable
