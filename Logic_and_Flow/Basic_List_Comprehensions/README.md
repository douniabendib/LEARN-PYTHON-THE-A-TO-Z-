# Basic List Comprehensions

## The Syntax
A list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. The basic syntax of a list comprehension is:
```python
new_list = [expression for item in iterable]
```
Here's a breakdown of the syntax:

- new_list: The new list that will be created.
- expression: The value to be included in new_list. This can be a modified version of item.
- for item in iterable: A loop that iterates over each element in the iterable (e.g., a list, tuple, or range).
- item: The current element being processed in the loop.
Here's a simple example:
```python
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)
# Output: [1, 4, 9, 16, 25]
```
In this example, the list comprehension creates a new list called squares by taking each element n from the numbers list and squaring it.

## Creating Simple Lists

Now that you know the syntax of list comprehensions, let’s dive into some simple examples to see how they can be used to create new lists quickly and efficiently.

Create a list of cube numbers:
```python
cubes = [x**3 for x in range(1, 6)]
print(cubes)
# Output: [1, 8, 27, 64, 125]
```
Create a list of strings from characters:
```python
chars = [char for char in "hello"]
print(chars)
# Output: ['h', 'e', 'l', 'l', 'o']
```
Generate a list of even numbers:
```python
evens = [x for x in range(2, 11, 2)]
print(evens)
# Output: [2, 4, 6, 8, 10]
```
Convert all items in a list to uppercase:
```python
words = ["apple", "banana", "cherry"]
uppercase = [word.upper() for word in words]
print(uppercase)
# Output: ['APPLE', 'BANANA', 'CHERRY']
```
List comprehensions make it easy to work with sequences, apply transformations, and even include conditions—all in one line!
