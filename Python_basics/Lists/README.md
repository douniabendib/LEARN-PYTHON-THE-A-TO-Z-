# List

## Declaring a List
A list is a collection of items, and it can contain values of different types, such as numbers, strings, or even other lists. Lists are created using square brackets [], and the items inside the list are separated with commas.
Here is an example of how to create a list:
```python
my_list = [1, 2, "three", True]
```
To check the length of the list, we can use the len() function:
```python
length = len(my_list)
```
The variable length will hold 4 because there are 4 elements in the list.

## Lists Continued
Sometimes when we're manually creating lists it can be hard to read if all the items are on the same line of code. We can declare the list using multiple lines if we want to:
```python
flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
]

player_ages = [
    23,
    18,
    31,
    42
]
```
Writing it this way helps with readability and organization, especially if there are many items or if some of the items are too long. Keep in mind this is just a styling change. The code will run correctly either way. 

## Accessing List Elements

In Python, we use lists to store multiple values in a single variable. Each value in a list is called an element, and each element has an index. The indices start from 0 to the length of the list minus one. For example take a look at the next list: 
```python
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
- Element a is at index 0
- Element b is at index 1
- ...
- Element g is at index 6
To access an element of a list, we can use its index within square brackets. For example, to access the first element of a list named my_list, we would use my_list[0].

Here's an example:
```python
my_list = [10, 20, 30, 40, 50]
element = my_list[2]
```
The variable element will hold the value 30 because it access the third element (which has an index of 2).

## List Length

The length of a List can be calculated using the len() function.
```python
fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3
```
The length of the list is equal to the number of items present. Don't be fooled by the fact that the length is not equal to the index of the last element, in fact, it will always be one greater.

## Modifying Lists

In addition to accessing the elements of a list, you can also modify them. To modify a specific element in a list, you can assign a new value to it using its index.

Here's an example:
```python
my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
print(my_list)
# ["apple", "orange", "cherry"]
```
banana was changed to an orange.

## List Methods
Lists are packed with many methods (functionalities). To access a method, write:
```python
some_list.method()
```
Here is a list of the basic methods:

- append(element) - adds an element to the end of the list
- clear() - removes all elements from the list
- pop(index) - removes an element at the specified index
- reverse() - reverses the order of the list
- sort() - sorts the list in ascending order

- Appending():

It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the .append() method:
```python
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']
```
- Pop():
.pop() is the opposite of .append(). Pop removes the last element from a list and returns it for use. For example:
```python
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'
```
- Clear():
Example of the clear method:
```python
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
# This will output []
```
- Sort():
Example of the sort method:
```python
my_list = [1, 9, 2, 3]
my_list.sort()
print(my_list)
# This will output [1, 2, 3, 9]
```
## No-Index Syntax
In my opinion, Python has the most elegant syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:
```python
trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple
```
tree, the variable declared using the in keyword, directly accesses the value in the list rather than the index of the value. If we don't need to update the item and only need to access its value then this is a more clean way to write the code.

