# Inheritance

## Basic Inheritance

Inheritance is a core concept in Object-Oriented Programming that allows a class to inherit attributes and methods from another class. This creates a parent-child relationship between classes.

The parent class (also called the base class or superclass) is the one being inherited from. The child class (also called the derived class or subclass) is the one that inherits from the parent.

Here's how to create a child class that inherits from a parent class:
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"I am {self.name}, an animal")

# Child class
class Dog(Animal):
    pass  # We don't need to add anything yet
```
In this example, Dog inherits from Animal. The syntax is simple - just put the parent class name in parentheses after the child class name. The Dog class automatically gets all the attributes and methods from Animal.

Let's see how we can use these classes:
```python
# Create an animal
generic_animal = Animal("Creature")
generic_animal.info()  # Output: I am Creature, an animal

# Create a dog
buddy = Dog("Buddy")
buddy.info()  # Output: I am Buddy, an animal
```
Notice that even though we didn't write an __init__ method or an info method for Dog, it still has those methods because it inherited them from Animal.

Inheritance helps you:

- Reuse code across classes
- Create hierarchies of related classes
- Organize code into logical parent-child relationships

## The super() Function

The super() function allows a child class to call methods from its parent class. This is useful when you want to extend parent functionality rather than completely replace it.

When overriding methods, the parent's method isn't automatically called. The super() function gives you a way to call it explicitly.

Common uses of super():

Calling the parent's __init__ method:
```python
class Animal:
   def __init__(self, name):
       self.name = name
class Dog(Animal):
   def __init__(self, name, breed):
       super().__init__(name)  # Call parent's __init__
       self.breed = breed
```
Extending a parent method:
```python
class Animal:
    def make_sound(self):
        print("Generic sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Call parent's method
        print("Woof!")        # Add dog-specific sound
```
The super() function helps you:

- Avoid duplicating code
- Ensure proper initialization
- Extend parent behavior
