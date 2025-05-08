# Functions

# What is function?

Function is a reusable block of code that performs a specific task. Functions help organize code into manageable sections and promote code reusability.

## Defining a Function:

You can define a function using the `def` keyword, followed by the function name and parentheses. If the function takes parameters, you specify them within the parentheses.

```python
def function_name(parameters):
    # code block
    return value
```

# Explanation of the `area_of_circle` Function:

The `area_of_circle` function calculates the area of a circle given its radius. Below is a detailed explanation of how the function works, including its definition, calculations, and usage. Here's a chronological explanation of what happens when the above code is executed:
1. def area_of_circle(r) 
	- The area_of_circle function is defined for later use, but not called. It accepts a single input, the arbitrarily named r. The body of the function (pi = 3.14... etc) is ignored for now.

2. radius = 5
	- A new variable called radius is created and set to the value 5.

3. area_of_circle(radius)
	- The area_of_circle function is called with radius (in this case 5) as the input. Finally, we jump back to the function definition.

4. def area_of_circle(r):
	- We will now start executing the body of the function, and r is set to 5.

5. pi = 3.14
	- A new variable called pi is created with a value of 3.14.

6. result = pi * r * r
	- Some simple math is evaluated (3.14 * 5 * 5) and stored in the result variable.

7. return result
	- The result variable is returned from the function as output.

8. area = area_of_circle(radius)
	- The returned value is stored in a new variable called area (in this case 78.5).

9. print(area)
	- The value of area is printed to the console.

# Multiple Parameters:

Functions can have multiple parameters ("parameter" being a fancy word for "input").The name of a parameter doesn't matter when it comes to which values will be assigned towhich parameter. It's position that matters. The first parameter will become the first value that's passed in, the second parameter is the second value that's passed in, and so on.
Here's an example with four parameters:

```python
def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro
```
It can be called like this:
```python
my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro) 

Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.
```

# Printing vs. Returning

Some new developers get hung up on the difference between print() and return.

It can be particularly confusing when the test suite we provide simply prints the output of your functions to the console. It makes it seem like print() and return are interchangeable, but they are not!

* print() is a function that:
	- Prints a value to the console.
	- Does not return a value.
* return is a keyword that:
	- Ends the current function's execution.
	- Provides a value (or values) back to the caller of the function.
	- Does not print anything to the console (unless the return value is later print()ed).

# Where to Declare Functions

You've probably noticed that a variable needs to be declared before it's used. For example, the following doesn't work:
```python
print(my_name)
my_name = 'Lane Wagner'
# NameError: 'my_name' is not defined
```
It needs to be:

```python
my_name = 'Lane Wagner'
print(my_name)
# Lane Wagner
```
Code executes in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after it has been defined.

# Order of Functions

All functions must be defined before they're used.

You might think this would make structuring Python code hard because the order of the functions needs to be just right. As it turns out, there's a simple trick that makes it super easy.

Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function last. That way all of the functions have been read by the Python interpreter before the first one is called.

#  Explanation of the fahrenheit_to_celsius.py

This script converts temperatures from Fahrenheit to Celsius. It provides a simple interface for testing the conversion with various Fahrenheit values.

## Overview

The script includes two main functions:

1. **`to_celsius(f)`**: Converts a given temperature from Fahrenheit to Celsius.
2. **`test(f)`**: Tests the conversion function and prints the results in a user-friendly format.

## Functions

### `to_celsius(f)`

- **Description**: This function takes a temperature in Fahrenheit and converts it to Celsius using the formula:

  \[
  C = \frac{5}{9} \times (F - 32)
  \]

- **Parameters**:
  - `f` (float): The temperature in Fahrenheit.

- **Returns**:
  - (float): The converted temperature in Celsius.

### `test(f)`

- **Description**: This function calls `to_celsius(f)` to convert the given Fahrenheit temperature and prints the result to the console.

- **Parameters**:
  - `f` (float): The temperature in Fahrenheit to test.

## Usage

To use the script, you can call the `test` function with any Fahrenheit value you want to convert. For example:

```python
test(100)  # Converts 100 degrees Fahrenheit to Celsius
```

# Explanation of the hours_to_secs.py

This script converts hours into seconds. It includes a function to perform the conversion and a test function to display the results.

## Overview

The script consists of two main functions:

1. **`hours_to_seconds(hours)`**: Converts a given number of hours into seconds.
2. **`test(hours)`**: Tests the conversion function and prints the result.

## Functions

### `hours_to_seconds(hours)`

- **Description**: This function takes a number of hours and converts it to seconds using the formula:
  
  \[
  \text{seconds} = \text{hours} \times 3600
  \]

- **Parameters**:
  - `hours` (float): The number of hours to convert.

- **Returns**:
  - (float): The equivalent number of seconds.

### `test(hours)`

- **Description**: This function calls `hours_to_seconds(hours)` to convert the given hours and prints the result.

- **Parameters**:
  - `hours` (float): The number of hours to test.

## Usage

To use the script, simply call the `test` function with the desired number of hours. For example:

```python
test(10)  # Converts 10 hours to seconds
```
# None Return

When no return value is specified in a function, it will automatically return None. For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value. The following code snippets all return the same value, None:

```python
def my_func():
    print("I do nothing")
    return None


def my_func():
    print("I do nothing")
    return


def my_func():
    print("I do nothing")
```

# Multiple Return Values

A function can return more than one value by separating them with commas.
```python
def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return (title, new_power)
def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()
```

# Parameters vs. Arguments

Parameters are the names used for inputs when defining a function. Arguments are the values of the inputs supplied when a function is called.

```python
# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)
```

# Default Values

In Python you can specify a default value for a function argument. It's nice for when a function has arguments that are "optional". You as the function definer can specify a specific default value in case the caller doesn't provide one.

A default value is created by using the assignment (=) operator in the function signature.
```python
def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)


get_greeting("lane@example.com", "Lane")
# Hello Lane welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Hello there welcome! You've registered your email: lane@example.com
```
f the second parameter is omitted, the default "there" value will be used in its place. As you may have guessed, for this structure to work, optional arguments (the ones with defaults) must come after all required arguments.
