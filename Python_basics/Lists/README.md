# Declaring a List
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
