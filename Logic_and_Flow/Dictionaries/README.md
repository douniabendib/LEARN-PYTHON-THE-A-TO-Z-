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

## Setting Dictionary Values

You don't need to create a dictionary with values already inside. It is common to create a blank dictionary then populate it later using dynamic values. The syntax is the same as getting data out of a key, just use the assignment operator (=) to give that key a value.

```python
planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False
```
## Modifying Dictionaries

Dictionaries in Python are not static; you can modify them after they are created. You can add new key-value pairs, update existing ones, or delete them.

Adding a new key-value pair:

```python
# Start with an empty dictionary
my_dict = {}

# Add a new key-value pair
my_dict["name"] = "Alice"
my_dict["age"] = 30

print(my_dict)
# Output: {'name': 'Alice', 'age': 30}
```
Updating an existing value:
```python
# Update the age
my_dict["age"] = 31

print(my_dict)
# Output: {'name': 'Alice', 'age': 31}
```
Deleting a key-value pair:
```python
# Delete the age
del my_dict["age"]

print(my_dict)
# Output: {'name': 'Alice'}
```
In these examples, we first add a new key-value pair to an empty dictionary. Then, we update the value of an existing key. Finally, we delete a key-value pair using the del keyword.

### Deleting Keys That Don't Exist
Notice that if you try to delete a key that doesn't exist, you'll get an error.
```python
names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["unknown"]
# ERROR HERE, key doesn't exist
```

## Dictionary Methods

Dictionaries, just like lists, come equipped with a variety of built-in methods to perform common operations. These methods can help you manipulate dictionaries more efficiently. Let's explore some of the key methods:

- keys(): Returns a view object that displays a list of all the keys in the dictionary.
```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)
# Output: dict_keys(['name', 'age', 'city'])
```
- values(): Returns a view object that displays a list of all the values in the dictionary.
```python
values = my_dict.values()
print(values)
# Output: dict_values(['Alice', 30, 'New York'])
```
- items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
```python
items = my_dict.items()
print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
```
- get(key, default): Returns the value for the specified key. If the key is not found, it returns the default value (or None if no default is specified).
```python
age = my_dict.get('age')
print(age)
# Output: 30

country = my_dict.get('country', 'USA')
print(country)
# Output: USA
```
- pop(key): Removes the element with the specified key and returns its value.
```python
city = my_dict.pop('city')
print(city)
# Output: 'New York'
print(my_dict)
# Output: {'name': 'Alice', 'age': 30}
```
## Nested Dictionaries
A nested dictionary is a dictionary within a dictionary. It allows you to organize complex data structures, making it easier to work with related information.

Example:
```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}

# Accessing a nested value
print(students["Alice"]["age"])  # Output: 20

# Adding a new key-value pair to a nested dictionary
students["Alice"]["major"] = "Math"
print(students["Alice"])  # Output: {'age': 20, 'grade': 'A', 'major': 'Math'}
```
Nested dictionaries are useful when you need to group related information together, such as storing details about students, employees, or products.

