# Python Numbers
In Python, numbers without a decimal point are called Integers - just like they are in mathematics.

Integers are simply whole numbers, positive or negative. For example, 3 and -3 are both examples of integers.

Arithmetic can be performed as you might expect:
- Addition
```python
2 + 1
# 3
```
- Subtraction
```python
2 - 1
# 1
```
- Multiplication
```python
2 * 2
# 4
```
- Division
```python
3 / 2
# 1.5 (a float)
```
# Numbers Review
* Integers
In Python, numbers without a decimal point are called Integers.

Integers are simply whole numbers, positive or negative. For example, 3 and -3 are both examples of integers.
* Floats
A float is, as you may have guessed, the number type that allows for decimal values.
```python
my_int = 5
my_float = 5.5
```

# Floor Division
Python has great out-of-the-box support for mathematical operations. This, among other reasons, is why it has had such success in artificial intelligence, machine learning, and data science applications.

Floor division is like normal division except the result is floored afterward, which means the result is rounded down to the nearest integer. The // operator is used for floor division.
```python
7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)
```
# Exponents
Python has built-in support for exponents - something most languages require a math library for.
```python
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9
```
# Changing in Place
It's fairly common to want to change the value of a variable based on its current value.
```python
player_score = 4
player_score = player_score + 1
# player_score now equals 5
player_score = 4
player_score = player_score - 1
# player_score now equals 3
```
Don't let the fact that the expression player_score = player_score - 1 is not a valid mathematical expression be confusing. It doesn't matter, it is valid code. It's valid because the way the expression should be read in English is:

Assign to player_score the current value of player_score minus 1

In this operation, the right-hand side (player_score - 1) is calculated first. Once we have the result, we update player_score with this new value.

# Plus Equals
Python makes reassignment easy when doing math. In JavaScript or Go, you might be familiar with the ++ syntax for incrementing a number variable by 1. In Python, we use the += in-place operator instead.
```python
star_rating = 4
star_rating += 1
# star_rating is now 5
```
* Other Operators
```python
star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0
```
# Scientific Notation
As we covered earlier, a float is a positive or negative number with a fractional part.

You can add the letter e or E followed by a positive or negative integer to specify that you're using scientific notation.
```python
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071
```
If you're not familiar with scientific notation, it's a way of expressing numbers that are too large or too small to conveniently write normally.

In a nutshell, the number following the e specifies how many places to move the decimal to the right for a positive number, or to the left for a negative number.

# Underscores for Readability
Python also allows you to represent large numbers in the decimal format using underscores as the delimiter instead of commas to make it easier to read.
```python
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```
# Logical Operators
You're probably familiar with the logical operators and and or.

Logical operators deal with boolean values, True and False.

The logical and operator requires that both inputs are True to return True. The logical or operator only requires that at least one input is True to return True.

For example:
```python
True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False
```
* Python Syntax
```python
print(True and True)
# prints True

print(True or False)
# prints True
```
# Nesting With Parentheses
We can nest logical expressions using parentheses.
```python
print((True or False) and False)
```
First, we evaluate the expression in the parentheses, (True or False). It evaluates to True:
```python
print(True and False)
```
True and False evaluates to False:
```python
print(False)
```
So, print((True or False) and False) prints "False" to the console.
