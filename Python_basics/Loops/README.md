# Loops

## For Loop
Sometimes when programming, it's necessary to perform the same or almost the same operation a couple of times.
To prevent writing the same thing over and over again, we can use loops.
The for loop has the following syntax:
```python
for i in range(start, end):
    code
```
The range(start, end) determines what is the start value and what is the end value. The i will receive all values from start to end (not including end) sequentially. For example:
```python
for i in range(0, 5):
    print(i)
```
It will execute the print statement 5 times:
```python
0
1
2
3
4
```
We can simplify the range(0, 5) to range(5):
```python
for i in range(5):
    print(i)
```
Loops have many use cases. For example, let's sum all the numbers from 1 to 100:
```python
sum_numbers = 0
for i in range(1, 101):
    sum_numbers += i
print(sum_numbers)
```
This will first loop through all numbers between 1 and 101 (not including 101) and sum all of them. Then it will print the sum_numbers variable.

# Whitespace in Python
The body of a for-loop must be indented, otherwise you'll get a syntax error. Not only that, but every line in the body of the loop must be indented in the same way - we use the "4 spaces" convention. Pressing the <tab> key should automatically insert 4 spaces.

Whitespace matters in Python.

# Range Continued
The range() function we've been using in our for loops actually has an optional 3rd parameter: the "step".
```python
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8
```
The "step" parameter determines how much to add to i in each iteration of the loop. You can even go backwards:
```python
for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1
```

