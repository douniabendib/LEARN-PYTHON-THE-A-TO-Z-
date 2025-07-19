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

## Mixins

Mixins are a special kind of multiple inheritance in Python used to "mix in" additional methods and properties from other classes. Unlike traditional inheritance, mixins don't define a standalone class but provide specific functionality to be added to other classes.

Key characteristics of mixins:

They're not meant to be instantiated on their own
They provide a specific set of related methods
They don't require constructor implementation
Their names often end with "Mixin" or "able" (e.g., PrintableMixin, Comparable)
Here's a simple example of a mixin that adds JSON serialization capabilities:
```python
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONSerializableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Now User has the to_json method
user = User("Alice", "alice@example.com")
print(user.to_json())
# Outputs: {"name": "Alice", "email": "alice@example.com"}
```
Mixins allow for code reuse across different class hierarchies and help avoid the complexity of deep inheritance trees.
