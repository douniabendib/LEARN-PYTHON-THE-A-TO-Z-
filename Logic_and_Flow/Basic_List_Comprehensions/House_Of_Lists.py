"""
Create a function named house_of_lists that takes a list 
of lists list_of_lists as an argument. Each inner list 
contains numbers. The function should use list comprehensions
 to perform the following operations:

Filter out inner lists that have a sum greater than 50.
From the remaining inner lists, extract numbers that are less than 5.
Combine all extracted numbers into a single list.
Return the combined list of numbers.
"""
def house_of_lists(list_of_lists):
    # Filter lists with a sum <= 50
    filtered_lists = [lst for lst in list_of_lists if sum(lst) <= 50]
    # Extract numbers < 5 from the filtered lists
    extracted_numbers = [num for lst in filtered_lists for num in lst if num < 5]
    # Return the combined list of numbers
    return extracted_numbers


print(house_of_lists([[10, 20, 30], [1, 2, 3], [5, 50, 5], [0, 3, 6, 9]]))
print(house_of_lists([[4, 4, 4], [100], [2, 3, 4], [10, 10, 10, 10]]))
