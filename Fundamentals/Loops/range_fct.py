"""
Create a program that performs the following tasks using range():

Print all numbers between 30 to 80 that are divisible by 4
Print the first 8 odd numbers starting from 15
Count backwards from 50 to 10, showing only numbers divisible by 5
Find the product of all numbers from 1 to 30 that are divisible by 3
When printing a number use the following code to print:
print(num, end=", ")
"""
# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
for i in range(30, 81):
    if i % 4 == 0:
        print(i, end=", ")
print()  # new line
# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
for num in range(15, 30, 2):
    print(num, end=", ")
print()  # new line
# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
for j in range(50, 9, -5):
    print(j, end=", ")
print()  # new line
# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
mul = 1
for k in range(3, 31, 3):
    if k % 3 == 0:
        mul *= k
print(mul)
print()
