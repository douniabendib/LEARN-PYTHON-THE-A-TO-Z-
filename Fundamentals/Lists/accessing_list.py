"""
Create a function named sum_elements that receives a list 
as an argument and prints the sum of all the elements in the list.

To iterate over a list, use the len() function inside the range() 
function
"""
def sum_elements(lst):
    res = 0
    for i in range(len(lst)):
        res += lst[i]
    print(res)

sum_elements([1, 2, 3, 4, 5])
