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
