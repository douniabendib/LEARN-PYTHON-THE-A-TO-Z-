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

## Basic Operations
Sets come with built-in operations that allow you to perform common set-related tasks efficiently. These operations include adding elements, removing elements, and checking for the presence of elements.

Adding an element to a set:
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}
```
Removing an element from a set: (raises an error if it does not exist!)
```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# Output: {1, 3}
```
Checking for the presence of an element:
```python
my_set = {1, 2, 3}
print(2 in my_set)
# Output: True
print(4 in my_set)
# Output: False
```
## Set Methods
Here are even more essential set methods:

- discard(element): Removes the specified element from the set if it exists. Does not raise an error if the element is not found.
```python
my_set = {1, 2, 3}
my_set.discard(3)    # Removes 3 from the set
my_set.discard(4)    # No error, even though 4 is not in the set
print(my_set)
# Output: {1, 2}
```
- pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
```python
my_set = {1, 2, 3}
element = my_set.pop()  # Removes and returns an arbitrary element
print(element)
# Output: 1 (or another element, as it's arbitrary)
print(my_set)
# Output: {2, 3} (or a different set, depending on the popped element)
```
- clear(): Removes all elements from the set, making it empty.
```python
my_set = {1, 2, 3}
my_set.clear()       # Removes all elements
print(my_set)
# Output: set()
```
## Mathematical Operations Part 1

Sets support mathematical operations such as union, intersection, difference, and symmetric difference. These operations are useful for comparing and combining sets in various ways.

- Union (| or union()): Combines the elements from both sets, excluding duplicates.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)
# Output: {1, 2, 3, 4, 5}
```
- Intersection (& or intersection()): Returns a set containing only the elements that are common to both sets.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)
# Output: {3}
```
- Difference (- or difference()): Returns a set containing the elements that are in the first set but not in the second set.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)
# Output: {1, 2}
```
- Symmetric Difference (^ or symmetric_difference()): Returns a set containing the elements that are in either of the sets, but not in both.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)
# Output: {1, 2, 4, 5}
```
