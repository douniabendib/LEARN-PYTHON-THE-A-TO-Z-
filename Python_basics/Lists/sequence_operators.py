"""
Create a program that receives a list of 
numbers as input and prints a new list that:

Contains the original list followed by its reverse
Has the first element of the original list inserted 
at the beginning and the last element inserted at the end
Repeats this entire sequence twice
"""
numbers = input("Enter a list of numbers: ").split()
combined_list = [numbers[0]] + numbers + numbers[::-1] + [numbers[-1]]
repeated_list = combined_list * 2
print(repeated_list)
