# Introduction to Decorators

Decorators are a way to modify or enhance functions and classes without changing their original code. They use the @ symbol.

Here is an example of a simple decorator: 
```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
```
Apply the decorator using @:
```python
@my_decorator
def say_hello():
    print("Hello!")
```
Call the decorated function:
```python
say_hello()
```
Output:
```python
Before function runs
Hello!
After function runs
```
The @my_decorator is equivalent to writing:
```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```
But the @ syntax is much cleaner and easier to read.

Key Point: Decorators wrap around functions to add extra functionality without modifying the original function code
