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

def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro

It can be called like this:

my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro) 
"""Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms."""

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

