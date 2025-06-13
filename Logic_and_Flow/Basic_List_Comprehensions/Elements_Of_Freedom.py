"""
Create a function named elements_of_freedom that processes 
a list of string elements according to specific rules.

Your function should:

Filter out elements that have fewer than 5 characters
Convert the remaining elements to uppercase
Remove any duplicate elements
Return a list of the unique uppercase elements
Use list operations to efficiently process the data.
"""
def elements_of_freedom(elements):
    # Step 1: Filter elements with length >= 5
    filtered_element = [word for word in elements if len(word) >= 5]
    # Step 2: Convert filtered elements to uppercase
    uppercase = [words.upper() for words in filtered_element]
    # Step 3: Create a list of unique elements
    unique_element = []
    for item in uppercase:
        if item not in unique_element:
            unique_element.append(item)
    # Step 4: Return the final result
    return unique_element


print(elements_of_freedom(["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"]))
