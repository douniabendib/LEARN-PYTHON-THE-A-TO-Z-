# Chapter 2 : Variables

## What are Variables?

Variable is a symbolic name associated with a value and is used to store data in a program.

### Key Characteristics of Variables:

- **Storage**: Variables act as storage locations for data values.

- **Naming**: Each variable has a name (identifier) that you use to access its value. Variable names must follow certain rules:
  - Must start with a letter (a-z, A-Z) or an underscore (_).
  - Can contain letters, numbers (0-9), and underscores.
  - Are case-sensitive (e.g., myVar and myvar are different variables).

- **Data Types**: Variables can store different types of data, including:
  - Integers: Whole numbers (e.g., 5, -3)
  - Floats: Decimal numbers (e.g., 3.14, -0.001)
  - Strings: Text data enclosed in quotes (e.g., "Hello, World!")
  - Booleans: True or False values (e.g., True, False)

- **Dynamic Typing**: In languages like Python, you do not need to declare the type of a variable explicitly. The interpreter determines the type based on the value assigned.

## Comments:

Comments in Python are used to explain code, making it easier to understand for yourself and others. They are ignored by the Python interpreter, meaning they do not affect the execution of the program. Here’s a detailed overview of how to use comments in Python:
- **Types of Comments in Python**:
1. Single-Line Comments: Single-line comments start with a hash mark (#).
2. Multi-Line Comments: You can use multiple single-line comments or triple quotes (""" or ''') to create a comment that spans multiple lines.

## Python Data Types in main.py

This document describes various data types used in the `main.py` file, along with the comments added in the code.

## What is Formatted String Literals?

Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

### Key Features of f-strings:

- **Expression Support**: You can include any valid Python expression inside the braces.
- **Calling Functions**: You can call functions within the braces.
- **Formatting Options**: You can use format specifications for numbers and dates.
- **Multiline f-strings**: You can also use f-strings over multiple lines.

## F-Strings in f_string.py

- Opening quotes must be preceded by an f.
- Variables within curly brackets have their values "interpolated" (injected) into the string.
- It's just a string with a special syntax.


