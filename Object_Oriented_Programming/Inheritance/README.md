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

## Method Overriding

Method overriding is a feature in inheritance where a child class provides its own implementation of a method that is already defined in its parent class. This allows the child class to change how the inherited method behaves.

To override a method:

1. Create a method in the child class with the same name as in the parent class
2. Give it the same parameters (although you can add more)
3. Implement the new behavior you want
Here's an example:
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some generic animal sound")
    
    def info(self):
        print(f"I am {self.name}")

# Child class with method overriding
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")  # Override the parent method
```
When you call the overridden method on a child object, Python uses the child's version instead of the parent's:
```python
# Create instances
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Call the methods
animal.make_sound()
# Output: Some generic animal sound
dog.make_sound()
# Output: Woof! Woof!

# Non-overridden methods still work normally
animal.info()
# Output: I am Generic Animal
dog.info()
# Output: I am Buddy
```
Method overriding allows you to:

- Customize inherited behavior for specific child classes
- Adapt parent class methods to fit the child class's needs
- Implement polymorphism (objects of different classes responding differently to the same method call)

## Multiple Inheritance

Multiple inheritance is a feature in Python that allows a class to inherit attributes and methods from more than one parent class. This powerful capability enables you to combine functionality from different classes.

Here's how you can implement multiple inheritance:
```python
# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"

# Parent class 2
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

# Child class inheriting from both parents
class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    
    def sing(self):
        return f"{self.name} is singing"
```
In this example, Bird inherits from both Animal and Flyable. It has access to the eat method from Animal and the fly method from Flyable. It also has its own sing method.

You can create an instance of Bird and call methods from both parent classes:
```python
sparrow = Bird("Sparrow", "House sparrow")
print(sparrow.eat())    # From Animal class
print(sparrow.fly())    # From Flyable class
print(sparrow.sing())   # Bird's own method
```

