"""
Write a recursive function named sum_nested that takes a nested list 
nested_list as an argument. The function should:

Add all the integers in the list, including integers in any sublists.
Return the total sum as an integer.
"""
def sum_nested(nested_list):
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            total_sum += sum_nested(element)  # Recursively sum the sublist
        else:
            total_sum += element  # Add the integer to the total sum
    return total_sum


print(sum_nested([10, 20, 30, 40]))
print(sum_nested([1, [2, 3], [4, [5, 6]], 7]))
print(sum_nested([]))
