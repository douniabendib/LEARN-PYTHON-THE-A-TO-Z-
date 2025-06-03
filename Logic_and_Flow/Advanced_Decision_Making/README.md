# Advanced Decision Making

## Ternary Operator

The ternary operator is a concise way to write simple if-else statements in a single line. It's a shorthand method that can make your code more compact and readable when used appropriately.

The syntax of the ternary operator is:
```python
value_if_true if condition else value_if_false
```
Here's how it works:

If the condition is true, the expression evaluates to value_if_true.
If the condition is false, the expression evaluates to value_if_false.
For example:
```python
age = 20
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)
```
In this example, if age is greater than or equal to 18, status will be assigned the value "Eligible". Otherwise, it will be assigned "Not Eligible".

The ternary operator is particularly useful for simple conditional assignments where you want to choose between two values based on a condition.

## Membership Checks

Membership checks in Python let you check if a value exists in a collection like a list, tuple, set, or dictionary using in and not in.

The in operator checks if a value exists:
```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
```
The not in operator checks if a value does not exist:
```python
numbers = [1, 2, 3]
print(4 not in numbers)  # True
```
For dictionaries, membership checks apply to keys by default:
```python
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)  # True
print("Alice" in my_dict)  # False
```
## Identity Checks

In Python, the is and is not operators are used to check the identity of objects. Unlike the == operator, which checks if two variables have the same value, the is operator checks if two variables refer to the exact same object in memory.

Basic usage of is:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True
print(a is c)  # Output: False
```
In this example, a and b refer to the same list object, so a is b returns True. However, a and c are different list objects with the same values, so a is c returns False.

Basic Usage of is not:
```python
x = 5
y = 5
z = 10

print(x is not y)  # Output: False
print(x is not z)  # Output: True
```
Here, x and y refer to the same integer object (due to Python's optimizations for small integers), so x is not y returns False. x and z are different objects, so x is not z returns True.

Identity checks are particularly useful when you want to determine if two variables are pointing to the same object in memory, rather than just having the same value.

