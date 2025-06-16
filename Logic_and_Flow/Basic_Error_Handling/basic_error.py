"""
Write a program that prompts the user to enter a number. 
Use a try-except block to handle cases where the input 
is not a valid integer.

If the user enters a valid integer, print "You entered: <number>".
If the user enters an invalid value (e.g., a string or special character), 
catch the exception and print "Invalid input! Please enter a valid number."
"""
try:
    user_input = input()  # Get user input
    number = int(user_input)  # Attempt to convert to integer
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
