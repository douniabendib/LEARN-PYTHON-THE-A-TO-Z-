"""
Create a function named filter_and_square_set that takes a set 
input_set as an argument. The function should iterate over the 
elements in the set, filter out even numbers, and square the 
remaining odd numbers. The function should return a new set 
containing only the squared values of the odd numbers from the input set.

For example, if the input set is {1, 2, 3, 4, 5}, the function 
should return {1, 9, 25}.
"""
def filter_and_square_set(input_set):
    # Create a new set to store the filtered and squared elements
    result_set = set()

    # Iterate over the elements in the input set
    for element in input_set:
        # Check if the element is odd
        if element % 2 != 0:
            # Square the odd element and add it to the result set
            result_set.add(element ** 2)

    # Return the result set
    return result_set


print(filter_and_square_set({1,2,3,4,5}))
