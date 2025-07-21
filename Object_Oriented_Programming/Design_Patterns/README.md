# Design Patterns

Design pattern is a generic repeatable solution to a frequently occurring problem in software design that is used in software engineering. It isn't a complete design that can be written in code right away. It is a description or model for problem-solving that may be applied in a variety of contexts.

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

## Factory Pattern

The Factory Pattern is a creational design pattern that provides an interface for creating objects without specifying their concrete classes.

Let's create a simple Factory class that produces different types of vehicles:

First, define our Vehicle base class:
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return f"{self.brand} {self.model}"
```
Next, create specific vehicle types:
```python
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.vehicle_type = "Car"
    
    def get_info(self):
        return f"{self.vehicle_type}: {super().get_info()}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.vehicle_type = "Motorcycle"
    
    def get_info(self):
        return f"{self.vehicle_type}: {super().get_info()}"
```
Now, implement the Factory class:
```python
class VehicleFactory:
    def create_vehicle(self, vehicle_type, brand, model):
        if vehicle_type.lower() == "car":
            return Car(brand, model)
        elif vehicle_type.lower() == "motorcycle":
            return Motorcycle(brand, model)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
```
Using the Factory:
```python
factory = VehicleFactory()
my_car = factory.create_vehicle("car", "Toyota", "Corolla")
print(my_car.get_info())  # Output: Car: Toyota Corolla
```
Using *args to Make Your Factory More Flexible
One limitation of our factory is that it's designed for objects that all take the same parameters. But what if different product types need different parameters?

We can improve our factory using Python's *args syntax to handle variable arguments:
```python
class FlexibleVehicleFactory:
    def create_vehicle(self, vehicle_type, *args):
        if vehicle_type.lower() == "car":
            # Cars need brand, model
            return Car(args[0], args[1])
        elif vehicle_type.lower() == "motorcycle":
            # Motorcycles need brand, model
            return Motorcycle(args[0], args[1])
        elif vehicle_type.lower() == "truck":
            # Trucks need brand, model, and payload capacity
            return Truck(args[0], args[1], args[2])
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
```
The *args approach allows our factory to:

- Handle products that require different numbers of parameters
- Simplify our interface to a single method
- Easily extend to new product types with different initialization needs
- This flexibility is especially valuable when your factory creates a diverse range of objects with varying constructor parameters.
