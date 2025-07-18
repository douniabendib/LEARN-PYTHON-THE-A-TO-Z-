class Student:
    """Create a complete student records management system that demonstrates all the encapsulation concepts"""

    def __init__(self, student_id, name):
        self.__id = student_id
        self.__name = name
        self.__grades = {}
        self.__enrolled = True  # Default to enrolled

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(self.__name) < 2:
           raise ValueError("Must be at least 2 characters long")
        self.__name = value

    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if not isinstance(value, bool):
           raise ValueError("Enrolled must be a boolean value.")
        self.__enrolled = value

    @property
    def grade_average(self):
        if not self.__grades:
           return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def add_grade(self, course, grade):
        """Add a grade for a specific course."""
        self.__grades[course] = grade

    def display_record(self):
        """Display the student's record."""
        enrolled_status = "Yes" if self.__enrolled else "No"
        num_courses = len(self.__grades)
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Enrolled: {enrolled_status}")
        print(f"Courses: {num_courses}")
        print(f"Grade Average: {self.grade_average:.2f}")


class StudentRegistry:
    """Create a StudentRegistry class that manages multiple students"""

    def __init__(self):
        self.__students = {}

    def add_student(self, student):
        """Add a student to the registry."""
        self.__students[student.id] = student

    def remove_student(self, student_id):
        """Remove a student by ID."""
        if student_id in self.__students:
           del self.__students[student_id]

    def get_student(self, student_id):
        """Return a student by ID."""
        return self.__student.get(student_id)

    def get_top_student(self):
        """Return the student with the highest grade average."""
        if not self.__students:
           return None
        return max(self.__students.values(), key=lambda student: student.grade_average)

    def display_all(self):
        """Display information for all students."""
        for student in self.__students.values():
            print(f"ID: {student.id}, Name: {student.name}, Average: {student.grade_average:.2f}")


# Test your implementation
# Create students
student1 = Student(1001, "Alice Smith")
student2 = Student(1002, "Bob Johnson")
student3 = Student(1003, "Charlie Brown")

# Add grades
student1.add_grade("Math", 90)
student1.add_grade("Science", 85)
student1.add_grade("English", 92)

student2.add_grade("Math", 78)
student2.add_grade("Science", 80)
student2.add_grade("English", 85)

student3.add_grade("Math", 95)
student3.add_grade("Science", 91)
student3.add_grade("English", 89)

# Display student records
print("Student Records:")
student1.display_record()
print()
student2.display_record()
print()
student3.display_record()
print()

# Test name validation
try:
    student1.name = "J"  # Too short
except ValueError as e:
    print(f"Name validation error: {e}")
print()

# Create registry and add students
registry = StudentRegistry()
registry.add_student(student1)
registry.add_student(student2)
registry.add_student(student3)

# Display all students
print("All Students in Registry:")
registry.display_all()
print()

# Get top student
top_student = registry.get_top_student()
print(f"Top Student: {top_student.name} (Average: {top_student.grade_average})")

# Remove a student
registry.remove_student(1002)  # Remove Bob
print("\nAfter removing student 1002:")
registry.display_all()
