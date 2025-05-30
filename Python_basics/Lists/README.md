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

## The Enumerate Function
The enumerate() function allows you to loop through a sequence (like a list, tuple, or string) while keeping track of the index position of each item.

without enumerate() we would access both the index and the value the following way:
```python
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```
enumerate() is a more elegant way to get both index and value:
```python
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```
Both examples will output:
```python
Index 0: apple
Index 1: banana
Index 2: orange
``` 

## Iterating Over Strings
String splitting allows you to break a string into a list, while joining lets you combine list items into a string.

The split() method divides a string into a list of substrings based on a delimiter.

Split by whitespace:
```python
text = "apple banana cherry"
fruits = text.split()
print(fruits)
# ['apple', 'banana', 'cherry']
```
Split with specific delimiter:
```python
data = "john,25,new york"
data = data.split(',')
print(data)
# ['john', '25', 'new york']
```

The join() method combines elements of an iterable into a single string.

Basic joining:
```python
words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)
# "Hello World Python"
```
Join with different separator:
```python
fruits = ['apple', 'banana', 'cherry']
line = ','.join(fruits)
print(line)
# "apple,banana,cherry"
```
## List Slicing Part 1

Slicing allows us to extract portions of a list using the following syntax: lst[start:stop]. For example consider this list:
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])
# Output: [2, 3, 4, 5]
```
This gets elements from index 2 (inclusive) to index 6 (exclusive)

Omitting start parameter:
```python
print(numbers[:5])
# Output: [0, 1, 2, 3, 4]
```
When start is omitted, slice begins from index 0

Omitting stop parameter:
```python
print(numbers[5:])
# Output: [5, 6, 7, 8, 9]
```
When stop is omitted, slice goes until the end.

## List Slicing Part 2

Slicing has another step parameter: lst[start:stop:step], For example consider this list:
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Gets every second element from index 1 to 8

print(numbers[1:8:2])
# Output: [1, 3, 5, 7]
```
Gets every third element from index 2:
```python
print(numbers[2::3])
# Output: [2, 5, 8]
```
Slicing also supports negative indices.

Counting from end:
```python
print(numbers[-3:])
# Output: [7, 8, 9]
```
Here, -3 means "start 3 positions from the end"

Count until end:
```python
print(numbers[:-2])    
# Output: [0, 1, 2, 3, 4, 5, 6, 7]
```
Here, -2 means "stop 2 positions from the end" (exclusive)

Reversing with negative step:
```python
print(numbers[::-1])
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
Empty space before first : means “start from beginning”
Empty space between : means “go until the end”
-1 means "move backwards one step at a time"

## Sequence Operators

Python provides several operators that can be used with sequences like lists, strings, and tuples.

Concatenation with the + operator joins two sequences together:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
```
After executing the above code, combined_list contains:
```python
[1, 2, 3, 4, 5, 6]
```
Repetition with the * operator repeats a sequence a specified number of times:

```python
numbers = [1, 2, 3]
repeated_numbers = numbers * 3
```
After executing the above code, repeated_numbers contains:

```python
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```
These operators work with other sequences too:
```python
# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# String repetition
stars = "*" * 5  # "*****"
```
## List Deletion
Python has a built-in keyword del that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []
```

# Tuples
A tuple is an immutable (read-only) ordered collection of elements. Unlike lists, once created, tuples cannot be modified.

Create a tuple with parentheses:
```python
fruits = ("apple", "banana", "cherry")
```
You can also create a tuple without parentheses:
```python
colors = "red", "green", "blue"
```
Access tuple elements using indexing (just like lists):
```python
first_fruit = fruits[0]  # "apple"
```
Remember, tuples are immutable, so you cannot modify elements:
```python
# This will cause an error
# fruits[0] = "orange"
```
A tuple with a single element needs a trailing comma:
```python
single_item = ("apple",)  # This is a tuple
not_a_tuple = ("apple")   # This is a string
```
