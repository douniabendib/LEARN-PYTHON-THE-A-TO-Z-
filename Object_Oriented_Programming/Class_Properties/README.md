# Class Properties

## Instance vs Class Variables

In Python classes, there are two main types of variables (attributes):

Class Variables belong to the class itself and are shared by all instances. They're defined within the class but outside any methods.

Instance Variables belong to individual objects (instances) and can have different values for each object. They're typically defined in the __init__ method using self.

Here's how they differ:
```python
class Student:
    # Class variable - shared by all instances
    school = "Python High School"
    
    def __init__(self, name, grade):
        # Instance variables - unique to each student
        self.name = name
        self.grade = grade
```
Let's see them in action:
```python
# Create student objects
alice = Student("Alice", "A")
bob = Student("Bob", "B")

# Access instance variables (different for each student)
print(alice.name)
# Output: Alice
print(bob.name)
# Output: Bob

# Access class variable (same for all students)
print(alice.school)
# Output: Python High School
print(bob.school)
# Output: Python High School
print(Student.school)
# Output: Python High School

# If we change the class variable
Student.school = "Python Academy"
print(alice.school)
# Output: Python Academy
print(bob.school)
# Output: Python Academy
```
Key differences:

- Class variables are shared among all instances
- Instance variables are unique to each instance
- Class variables are defined once, instance variables for each object
