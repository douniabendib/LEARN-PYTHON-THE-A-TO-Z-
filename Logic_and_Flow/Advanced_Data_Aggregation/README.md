# Advanced Data Aggregation

## Using Sum

The sum() function is a built-in function that allows you to quickly calculate the sum of elements in an iterable, such as a list or a tuple. It provides a concise way to add up numeric values.

Basic Usage:
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
# Output: 15
```
In this example, the sum() function calculates the sum of all elements in the numbers list.
- Using a Starting Value:

You can also provide a second argument to sum(), which serves as the starting value for the sum. This is useful when you want to add the elements of an iterable to an initial value.
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers, 10)
print(total)
# Output: 25
```
In this case, the sum() function starts with the value 10 and adds all elements from the numbers list to it.
