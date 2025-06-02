"""
Write a program that:

Takes two numbers as input
Creates a list of numbers from the first input to the second input (not including)
Finds and prints the first even number greater than 5
Then, in a separate loop, find and print the first number divisible by 7
"""
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

for i in range(number1, number2):
    if i % 2 == 0 and i > 5:
       print(f"First even number greater than 5: {i}")
       break

for j in range(number1, number2):
    if j % 7 == 0:
       print(f"First number divisible by 7: {j}")
       break
