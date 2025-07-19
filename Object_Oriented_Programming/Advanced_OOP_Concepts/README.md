# Advanced OOP Concepts

## Composition vs Inheritance

Object-oriented programming offers two main approaches for code reuse: inheritance and composition.

* Inheritance creates an "is-a" relationship:
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):  # Dog "is an" Animal
    def bark(self):
        return "Woof!"
```
* Composition creates a "has-a" relationship:
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:  # Car "has an" Engine
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        return self.engine.start()
```
Key differences:

- Inheritance: tight coupling, best for true hierarchies
- Composition: flexible, easier to modify, recommended in most cases
The principle "Composition over Inheritance" suggests favoring composition for its flexibility and looser coupling.
