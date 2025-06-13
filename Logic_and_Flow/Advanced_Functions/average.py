"""
Create a lambda function named average that takes four arguments,
 a, b, c, and d, and returns their average (mean). 
After defining the lambda function, call it with the values 
10, 15, 20, and 25, and print the result.
"""
# Create a lambda function that calculates the average of four numbers
average = lambda a, b, c, d: (a + b + c + d) / 4

# Call the lambda function with the values 10, 15, 20, and 25
result = average(10, 15, 20, 25)

# Print the result
print(result)
