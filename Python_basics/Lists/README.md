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

