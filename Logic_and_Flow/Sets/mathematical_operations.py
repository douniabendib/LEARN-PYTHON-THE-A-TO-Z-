"""
Create a function named set_operations that takes two sets, set1 
and set2, as arguments. The function should perform the following 
operations:

Calculate the union of set1 and set2.
Calculate the intersection of set1 and set2.
Calculate the difference of set1 and set2 (elements in set1 but 
not in set2).
Calculate the symmetric difference of set1 and set2.
Return a dictionary containing the results of these operations, 
with the keys "union", "intersection", "difference", 
and "symmetric_difference".
"""
def set_operations(set1, set2):
    # Calculate the union
    union_result = set1 | set2

    # Calculate the intersection
    intersection_result = set1 & set2

    # Calculate the difference
    difference_result = set1 - set2

    # Calculate the symmetric difference
    symmetric_difference_result = set1 ^ set2

    # Return a dictionary containing the results
    return {
        "union": union_result,
        "intersection": intersection_result,
        "difference": difference_result,
        "symmetric_difference": symmetric_difference_result
    }


print(set_operations({1, 2, 3, 4}, {3, 4, 5, 6}))
