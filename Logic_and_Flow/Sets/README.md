# Sets

## What is a Set?

A set is a collection of unique elements. This means that a set cannot contain duplicate values. Sets are useful when you need to store a collection of items and ensure that each item appears only once.

Think of a set as a group of distinct items. For example, if you have a basket of fruits and you want to make sure you only have one of each type, you would use a set. In Python, sets are defined using curly braces {}, similar to dictionaries, but without key-value pairs.

Here's an example of how to create a set:
```python
# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Creating a set of strings
fruits = {"apple", "banana", "cherry"}

# Creating an empty set
empty_set = set()
```
In the first example, numbers is a set containing the numbers 1 through 5. In the second example, fruits is a set containing the strings "apple", "banana", and "cherry". The third example shows how to create an empty set using the set() constructor. Note that you cannot create an empty set using empty curly braces {} because that would create an empty dictionary instead.
