# Basic Error Handling

## What is Error Handling?

Error handling is a crucial aspect of programming that involves responding to and recovering from error conditions in your code. In Python, errors are managed using a system of exceptions. An exception is an event that occurs during the execution of a program, disrupting the normal flow of the program's instructions.

When an error occurs, Python creates an exception object. If the exception is not handled, the program will terminate and display an error message. Proper error handling allows your program to detect errors, handle them gracefully, and continue running.

Common types of exceptions include TypeError, ValueError, IOError, and ZeroDivisionError. For example, a TypeError occurs when an operation is performed on a value of an inappropriate type, and a ZeroDivisionError occurs when a number is divided by zero.

Here's a simple example of an error that occurs when trying to convert a string that does not represent a number into an integer:
```python
s = "abc"
n = int(s)  # This will raise a ValueError
print(n)
```
In this example, the int() function cannot convert the string "abc" into an integer, so it raises a ValueError. Without error handling, this exception would cause the program to crash.

## Errors and Exceptions in Python
You've probably encountered some errors in your code from time to time if you've gotten this far in the course. In Python, there are two main kinds of distinguishable errors:

- Syntax errors
- Exceptions

## Syntax Errors
You probably know what these are by now. A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.
```python
this is not valid code, so it will error
```
If I try to run that sentence as if it were valid code I'll get a syntax error:
```python
this is not valid code, so it will error
      ^
SyntaxError: invalid syntax
```
## The Try and Except Block

The try-except block in Python allows you to handle exceptions and prevent your program from crashing. Code that might raise an exception is placed inside the try block, and the except block handles the error if it occurs.

Here’s the basic structure:
```python
try:
    # Code that might cause an exception
    risky_code()
except ExceptionType:
    # Code to handle the exception
    handle_error()
```
Example:
```python
try:
    num = int("abc")  # This raises a ValueError
except ValueError:
    print("Invalid input! Please enter a number.")
```
Output:
```python
Invalid input! Please enter a number.
```
In this example, instead of crashing, the program catches the ValueError and prints a friendly message. Use try-except to handle specific exceptions and keep your program running smoothly.

## Handling Multiple Exceptions

In Python, we can handle different types of exceptions in separate except blocks. This allows us to respond differently based on the specific error that occurs.

Start with a basic try-except structure:
```python
try:
    # Code that might raise exceptions
    pass
except Exception as e:
    # Handle any exception
    pass
```
To handle multiple exceptions, add specific except blocks:
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
You can also catch multiple exception types in a single except block:
```python
try:
    # Some code
    pass
except (ValueError, TypeError):
    print("Invalid input type!")
```
The order of except blocks matters - always place more specific exceptions before more general ones.

## Different Types of Exceptions
We haven't covered classes and objects yet, which is what an Exception really is at its core. We'll go more into that in the course on object-oriented programming.

For now, what is important to understand is that there are different types of exceptions, and we can handle them differently depending on the situation. Some exceptions are more specific, like ZeroDivisionError (which happens when you divide by zero) or IndexError (which happens when you try to access a list element at an invalid index—either too high or too low). Others are more general, like the base Exception.

### Syntax
```python
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)
```
Which will print:
```python
0 division
index error 
```
## Why Specific Exceptions Come First
When handling exceptions, it’s important to catch the most specific ones first, because Python stops checking once it finds a matching exception handler. If you catch a more general Exception first, any specific errors will never get handled individually.

For example:
```python
try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")
```

In this case, the general Exception will catch the error before the IndexError can be reached, and the message “Index error” will never be printed. Always handle the most specific exception first!

## Alias Exception Messages
As seen in the example, you can also access the error using as, like this:
```python
except Exception as e:
    print(e)
```
The default behavior of print is that it will print the string representation of whatever object is passed to it. In this case, it will print the error message.

