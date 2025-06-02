# Dictionary

## What is a Dictionary?

A dictionary in Python is a collection of data that stores data in key-value pairs. Unlike lists, which use indices to access elements, dictionaries use keys. Each key in a dictionary must be unique, and it is associated with a value.

Think of a real-world dictionary. You look up a word (the key) to find its meaning (the value). In Python, a dictionary works similarly. For example, you can have a dictionary where the keys are names of countries and the values are their capitals.

Dictionaries are useful when you have data that is naturally paired together and when you need to quickly access a value by knowing its associated key.

## Creating a Dictionary

To create a dictionary in Python, you use curly braces {} and specify the key-value pairs within them. Each key-value pair is written as key: value, and multiple pairs are separated by commas.

Here's how you can create a dictionary:
```python
# Creating a dictionary of country capitals
country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Creating a dictionary of employee information
employee = {
    "name": "John Doe",
    "age": 30,
    "position": "Software Engineer"
}

# Creating an empty dictionary
empty_dict = {}
```
In the first example, country_capitals is a dictionary with country names as keys and their capitals as values. In the second example, employee is a dictionary containing information about an employee. The third example shows how to create an empty dictionary, which can be useful when you want to add items to it later.

## Accessing Values
In a dictionary, each key is associated with a value. To access a value, you use its key. This is similar to how you would look up a word in a physical dictionary to find its definition.

Here's how you can access values in a Python dictionary:
```python
# Dictionary of country capitals
country_capitals = {
 "USA": "Washington, D.C.",
 "France": "Paris",
 "Japan": "Tokyo"
}

# Accessing values using keys
print(country_capitals["USA"])
print(country_capitals["France"])

# Accessing a value that does not exist
# print(country_capitals["Germany"])  # This will cause an error
```
In this example, we access the capital of the USA by using the key "USA". If you try to access a key that does not exist in the dictionary, Python will raise a KeyError.
