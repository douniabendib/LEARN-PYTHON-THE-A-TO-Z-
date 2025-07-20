# Design Patterns

## Singleton Pattern

Singleton Pattern

The Singleton pattern ensures a class has only one instance and provides a global point of access to it.

Create a basic Singleton class:
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
Create two instances of the Singleton class:
```python
singleton1 = Singleton()
singleton2 = Singleton()
```
Check if both variables reference the same object:
```python
print(singleton1 is singleton2)  # True
```
The output confirms that singleton1 and singleton2 reference the same object instance.
