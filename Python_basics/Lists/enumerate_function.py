"""
Write a program that receives a list of words as input (given), 
and prints a list of the indices of the words that are either 
longer than 3 characters or start with the letter 'a' (case-sensitive).

To check if a string starts with some substring 
use: str.startswith("substring")
"""
lst = input("Enter: ").split()

new_list = []
for index, item in enumerate(lst):
    if len(item) > 3 or item.startswith('a'):
       new_list.append(index)

print(new_list)
