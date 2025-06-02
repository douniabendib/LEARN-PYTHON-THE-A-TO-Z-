# Comparison Operators
When coding it's necessary to be able to compare two values. Boolean logic is the name for these kinds of comparison operations that always result in True or False.

The operators:

- "<" => "less than"
- ">" => "greater than"
- "<=" => "less than or equal to"
- ">=" => "greater than or equal to"
- "==" => "equal to"
- "!=" => "not equal to"
For example:
```python
5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True
```
# Comparison Operator Evaluations
When a comparison happens, the result of the comparison is just a boolean value, it's either True or False.

Take the following two examples:
```python
is_bigger = 5 > 4
is_bigger = True
```
In both of the above cases, we're creating a Boolean variable called is_bigger with a value of True.

Because 5 is greater than 4, is_bigger is assigned the value of True.

# Comparison Practice
```python
car_size = 4
truck_size = 5
is_smaller = car_size < truck_size
# is_smaller is True
```
# If Statements
It's often useful to only execute code if a certain condition is met:
```python
if CONDITION:
	# do some stuff here

# code after the if block may still run regardless
```
For example, in this code:
```python
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")
```
if boss_health is greater than 0, then this will be printed:
```python
Ganondorf is alive!
```
Otherwise, this will be printed:
```python
Ganondorf is unalive!
```
Without a return in the if block, Ganondorf is unalive would always be printed:
```python
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
    print("Ganondorf is unalive!")
```
This code could print both messages:
```python
Ganondorf is alive!
Ganondorf is unalive!
```
When you only want code within an if block to run, use return to exit the function early.

# If-Else

An if statement can be followed by zero or more elif (which stands for "else if") statements, which can be followed by zero or one else statements.
For example:
```python
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")
```
First the if statement is evaluated. If it is True then the if statement's body is executed and all the other elifs and the else are ignored.

If the first if is false then the next elif is evaluated. Likewise, if it is True then its body is executed and the rest are ignored.

If none of the if or elif statements evaluate to True then the final else statement will be the only body executed.

Here are some basic rules with if/else blocks.
- You can't have an elif or an else without an if
- You can have an else without an elif
Remember, to check if two values are the same use the == operator.

