"""
Create a program that receives a list of numbers as input (given), 
and prints the sum of all even numbers in the list.
"""
numbers = input("Enter a list of numbers: ").split(',')
res = 0
for num in numbers:
    if int(num) % 2 == 0:
       res += int(num)
print(res)
