# Advanced Decision Making

## Ternary Operator

The ternary operator is a concise way to write simple if-else statements in a single line. It's a shorthand method that can make your code more compact and readable when used appropriately.

The syntax of the ternary operator is:
```python
value_if_true if condition else value_if_false
```
Here's how it works:

If the condition is true, the expression evaluates to value_if_true.
If the condition is false, the expression evaluates to value_if_false.
For example:
```python
age = 20
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)
```
In this example, if age is greater than or equal to 18, status will be assigned the value "Eligible". Otherwise, it will be assigned "Not Eligible".

The ternary operator is particularly useful for simple conditional assignments where you want to choose between two values based on a condition.

