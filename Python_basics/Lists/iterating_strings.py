"""
Create a program that takes two inputs: a string of numbers separated
 by spaces, and a prefix string. The program should split the number 
string into individual numbers, add the prefix to each number, then 
join these modified numbers back into a single string separated 
by spaces. Finally, print the resulting string.
"""
numbers = input("Enter a numbers separated by space: ")
prefix = input("Enter a prefix: ")

new_numbers = numbers.split()
new_list = []
for num in new_numbers:
    new_list.append(prefix + num)
result = ' '.join(new_list)
print(result)
