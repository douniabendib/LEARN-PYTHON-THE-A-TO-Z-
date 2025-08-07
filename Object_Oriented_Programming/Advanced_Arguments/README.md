<h1>The *args</h1>

# The args
The *args parameter allows a method to accept any number of positional arguments. The asterisk collects all extra positional arguments into a tuple.

Here is an example of a method using *args:
```python
class Calculator:
    def add_numbers(self, *args):
        return sum(args)
    
    def show_numbers(self, *args):
        for i, num in enumerate(args):
            print(f"Number {i+1}: {num}")
```
Call the method with different numbers of arguments:
```python
calc = Calculator()
result1 = calc.add_numbers(1, 2, 3)
result2 = calc.add_numbers(10, 20, 30, 40, 50)
print(result1)  # 6
print(result2)  # 150
#The *args collects all arguments into a tuple:
calc.show_numbers(5, 10, 15, 20)
```
Output:
```python
Number 1: 5
Number 2: 10
Number 3: 15
Number 4: 20
```
Combine regular parameters with *args:
```python
class Logger:
    def log_message(self, level, *messages):
        print(f"[{level}]", end=" ")
        for message in messages:
            print(message, end=" ")
        print()  # New line

logger = Logger()
logger.log_message("INFO", "User", "logged", "in")
logger.log_message("ERROR", "Connection", "failed")
```
Use *args in constructor methods:
```python
class Team:
    def __init__(self, team_name, *players):
        self.team_name = team_name
        self.players = list(players)
    
    def show_team(self):
        print(f"Team: {self.team_name}")
        for player in self.players:
            print(f"- {player}")

team = Team("Warriors", "Alice", "Bob", "Charlie", "Diana")
team.show_team()
```
Output:
```python
6
150
Number 1: 5
Number 2: 10
Number 3: 15
Number 4: 20
[INFO] User logged in 
[ERROR] Connection failed 
Team: Warriors
- Alice
- Bob
- Charlie
- Diana
```
You can also unpack arguments when calling methods:
```python
numbers = [1, 2, 3, 4, 5]
result = calc.add_numbers(*numbers)  # Unpacks the list
print(result)  # 15
```
Key Point: *args collects any number of positional arguments into a tuple. Use it when you don't know how many arguments will be passed to a method. The name args is conventional - you could use any name after the asterisk, but args is the standard.

## The kwargs

The **kwargs parameter allows a method to accept any number of keyword arguments. The double asterisk collects all extra keyword arguments into a dictionary.

Here is an example of a method using **kwargs:
```python
class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.details = kwargs
    
    def show_info(self):
        print(f"Name: {self.name}")
        for key, value in self.details.items():
            print(f"{key}: {value}")
```
Call the method with different keyword arguments:
```python
person1 = Person("Alice", age=25, city="New York", job="Engineer")
person2 = Person("Bob", age=30, country="Canada")

person1.show_info()
print()
person2.show_info()
```
The **kwargs collects all keyword arguments into a dictionary:
```python
class Config:
    def __init__(self, **kwargs):
        self.settings = kwargs
    
    def get_setting(self, key, default=None):
        return self.settings.get(key, default)
    
    def show_all_settings(self):
        for key, value in self.settings.items():
            print(f"{key} = {value}")

config = Config(debug=True, max_users=100, timeout=30)
config.show_all_settings()
```
Combine regular parameters, *args, and **kwargs:
```python
class Logger:
    def log(self, level, *messages, **options):
        # Regular parameter: level
        # *args: messages
        # **kwargs: options
        
        timestamp = options.get('timestamp', False)
        color = options.get('color', 'default')
        
        if timestamp:
            print("[2024-01-01 12:00:00]", end=" ")
        
        print(f"[{level}]", end=" ")
        
        for message in messages:
            print(message, end=" ")
        
        if color != 'default':
            print(f"(color: {color})")
        else:
            print()

logger = Logger()
logger.log("INFO", "User", "logged", "in", timestamp=True, color="green")
logger.log("ERROR", "Connection", "failed", timestamp=False)
```
Use **kwargs for flexible object initialization:
```python
class Product:
    def __init__(self, name, price, **features):
        self.name = name
        self.price = price
        self.features = features
    
    def describe(self):
        print(f"{self.name} - ${self.price}")
        if self.features:
            print("Features:")
            for feature, value in self.features.items():
                print(f"  {feature}: {value}")

laptop = Product("Gaming Laptop", 1299, 
                brand="TechCorp", 
                ram="16GB", 
                storage="1TB SSD",
                graphics="RTX 4060")
laptop.describe()
```
Output:
```python
Name: Alice
age: 25
city: New York
job: Engineer

Name: Bob
age: 30
country: Canada
debug = True
max_users = 100
timeout = 30
[2024-01-01 12:00:00] [INFO] User logged in (color: green)
[ERROR] Connection failed 
Gaming Laptop - $1299
Features:
  brand: TechCorp
  ram: 16GB
  storage: 1TB SSD
  graphics: RTX 4060
```
You can also unpack dictionaries when calling methods:
```python
settings = {"debug": True, "verbose": False, "log_level": "INFO"}
config2 = Config(**settings)  # Unpacks the dictionary
config2.show_all_settings()
#Output:

debug = True
verbose = False
log_level = INFO
```
Key Point: **kwargs collects any number of keyword arguments into a dictionary. Use it when you want flexible method signatures that can accept various named parameters. The name kwargs is conventional - you could use any name after the double asterisk, but kwargs is the standard
