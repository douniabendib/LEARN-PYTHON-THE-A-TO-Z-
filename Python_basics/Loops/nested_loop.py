"""
Write a function named print_pattern that prints
a rectangle pattern of stars (*).

The function should:

Take two parameters: rows and cols (both integers)
Use nested loops to print a rectangle with the given dimensions
Each row should contain cols stars
The pattern should have rows rows in total
"""

def print_pattern(rows, cols):
   for i in range(rows):
       row_string = ""
       for j in range(cols):
           row_string += '*'
       print(row_string)

# Get input for rows and columns
rows = int(input("Enter a number of rows: "))
cols = int(input("Enter a number of cols: "))

# Call the function
print_pattern(rows, cols)
