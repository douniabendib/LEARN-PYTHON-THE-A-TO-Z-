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

