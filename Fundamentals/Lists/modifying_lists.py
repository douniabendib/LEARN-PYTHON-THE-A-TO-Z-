"""
Create a function named change_element that receives 3 arguments:

First argument is a list
Second argument is an index
Third argument is another list
The function should replace the element at the given index 
in the first list with the first element from the second list.

Example:

change_element([1, 2, 3], 1, [5, 6, 7]) should return [1, 5, 3]
"""
def change_element(list1, index, list2):
    list1[index] = list2[0]
    return list1


print(change_element([1, 2, 3], 1, [5, 6, 7]))
