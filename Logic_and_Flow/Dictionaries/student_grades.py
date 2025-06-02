"""
In this challenge, you'll work with a dictionary of student grades 
to practice essential dictionary operations.

Follow these steps:

Create a dictionary named grades with these initial key-value pairs:
"Alice": 85
"Bob": 90
"Charlie": 78
Print all student names (keys) and grades (values) using 
dictionary methods.
Add a new student "Diana" with a grade of 92.
Use the get() method to retrieve and print Bob's grade.
Remove "Charlie" from the dictionary using the pop() method and 
print the updated dictionary.
Ensure your output matches the expected format shown in the example.
"""
# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades here
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Step 2: Access All Keys and Values
# Print all students and grades
print(f"Students: {grades.keys()}")
print(f"Grades: {grades.values()}")

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92
# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() method
bob_grades = grades.get("Bob")
print(f"Bob's grade: {bob_grades}")

# Step 5: Remove a Student
# Remove Charlie using pop() method
# Print the updated dictionary
grades.pop("Charlie")
print(f"Updated grades: {grades}")
