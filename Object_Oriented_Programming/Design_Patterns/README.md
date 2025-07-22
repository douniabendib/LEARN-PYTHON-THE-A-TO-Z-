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

## Observer Pattern

### Python Object Oriented Programming Design Patterns Observer Pattern
### Lesson Body:
The Observer Pattern is a behavioral design pattern where an object (the subject) maintains a list of dependents (observers) and notifies them of state changes.

Create a Subject class that manages observers:
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
```
Now create a method to notify all observers:
```python
def notify(self, message):
    for observer in self._observers:
        observer.update(message)
```
Define an Observer interface:
```python
class Observer:
    def update(self, message):
        pass
```
Create a concrete observer class:
```python
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")
```
Usage example:
```python
# Create subject
subject = Subject()

# Create observers
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

# Attach observers to subject
subject.attach(observer1)
subject.attach(observer2)

# Notify all observers
subject.notify("Hello Observers!")
```
Output:
```python
Observer 1 received: Hello Observers!
Observer 2 received: Hello Observers!
```

## Strategy Pattern

### Python Object Oriented Programming Strategy Pattern

* Lesson Body:
The Strategy Pattern is a behavioral design pattern that enables selecting an algorithm's behavior at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.

First, let's create an abstract strategy interface:
```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```
Now, let's implement concrete strategies:
```python
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card: {self.card_number}")
        return True
```
Create another payment strategy:
```python
class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal account: {self.email}")
        return True
```
Now, create a context class that will use these strategies:
```python
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        else:
            raise ValueError("No payment strategy set")
```
