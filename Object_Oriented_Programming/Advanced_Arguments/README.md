<h1>The *args</h1>

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
```
The *args collects all arguments into a tuple:
```python
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
