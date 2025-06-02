"""
Write a function named reverse which gets a list of numbers
 as argument and returns the reversed list.

For example, for [1, 2, 3], the expected output is [3, 2, 1].
"""
def reverse(lst):
    # Write code here
    reversed_list = []
    for i in range(len(lst)):
        reversed_list.append(lst[len(lst) - i - 1])
    return reversed_list

print(reverse([1, 2, 3]))
