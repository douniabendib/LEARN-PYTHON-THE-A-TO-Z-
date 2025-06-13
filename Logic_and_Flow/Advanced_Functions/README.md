# Advanced Functions

## Returning Multiple Values

In Python, a function can return multiple values. This is achieved by packaging the values into a tuple and returning the tuple. When the function is called, the returned tuple can be unpacked into separate variables.

Here's an example of a function that returns multiple values:
```python
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age

person_name, person_age = get_name_and_age()
print(person_name)
# Output: Alice
print(person_age)
# Output: 30
```
In this example, the function get_name_and_age returns the name and age values as a tuple. When we call the function, we unpack the returned tuple into the variables person_name and person_age.

Returning multiple values is useful when you need to return more than one piece of information from a function. Instead of creating a complex data structure like a list or a dictionary, you can simply return the values as a tuple.

## Lambda Functions Part 1

A lambda function is a small, anonymous function defined using the lambda keyword. Lambda functions can take any number of arguments but can only have one expression. They are useful for creating simple, one-line functions without the need for a full function definition using the def keyword.

The syntax of a lambda function is:
```python
lambda arguments: expression
```
Here's a breakdown of the syntax:

- lambda: The keyword that indicates the start of a lambda function definition.
- arguments: A comma-separated list of arguments, similar to the parameters in a regular function definition.
- expression: A single expression that is evaluated and returned as the result of the lambda function.
Here's an example of a lambda function that adds two numbers:
```python
add = lambda x, y: x + y
result = add(5, 3)
print(result)
# Output: 8
```
In this example, the lambda function takes two arguments, x and y, and returns their sum. The lambda function is assigned to the variable add, which can then be called like a regular function.

Lambda functions are often used in situations where a short, throwaway function is needed, such as with higher-order functions like map, filter, and reduce.
