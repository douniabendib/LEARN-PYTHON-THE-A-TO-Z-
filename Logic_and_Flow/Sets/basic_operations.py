"""
Create a function named manage_list that takes three arguments: list1
 (a list of integers), element_to_append, and index_to_remove. 
The function should perform the following operations:

Append element_to_append to the end of list1.
Attempt to remove the element at index index_to_remove from list1. 
If the index is out of range, do nothing.
Check if list1 has more than 3 elements. 
If it does, return the string "The list has more than 3 elements". 
Otherwise, return the string "The list has 3 or fewer elements".
"""
def manage_list(list1, element_to_append, index_to_remove):
    # Append element_to_append to list1
    list1.append(element_to_append)

    # Attempt to remove element at index_to_remove from list1
    if 0 <= index_to_remove < len(list1):
        list1.pop(index_to_remove)

    # Check if list1 has more than 3 elements
    if len(list1) > 3:
        return "The list has more than 3 elements"
    else:
        return "The list has 3 or fewer elements"


print(manage_list([1,2,3], 4, 5))
