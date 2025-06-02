"""
Create a program that takes a list and prints:

For lists with 5 or more items: the first two and last two items.
For lists with less than 5 items: the first and last item only.
"""
input_list = input("Enter: ").split(', ')
if len(input_list) >= 5:
   print(input_list[0:2] + input_list[-2:])
else:
   print([input_list[0], input_list[-1]])
