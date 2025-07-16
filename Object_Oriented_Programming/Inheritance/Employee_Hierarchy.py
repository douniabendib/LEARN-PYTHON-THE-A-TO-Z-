
class Person:
    """Create a base Person class"""

    def __init__(self, name, age):
        """Constructor that sets name and age parameters"""
        self.name = name
        self.age = age

    def introduce(self):
        """Method introduce() that return name and age"""
        return f"Hi, I'm {self.name}, {self.age} years old."


class Employee(Person):
    """Create an Employee class that inherits from Person"""

    def __init__(self, name, age, employee_id, salary):
        """Adds attributes for employee_id and salary using super()"""
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def introduce(self):
        """Overrides introduce() to return the parent's introduction plus employee ID"""
        return super().introduce() + f"I work with employee ID {self.employee_id}."

    def calculate_paycheck(self):
        """Returns the monthly salary"""
        return self.salary / 12


class Manager(Employee):
    """Create a Manager class inherits from Employee"""

    def __init__(self, name, age, employee_id, salary, department):
        """Adds a department attribute using super()"""
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def calculate_paycheck(self):
        """Overrides calculate_paycheck() to include a 20% bonus"""
        return (self.salary * 1.2) / 12

    def manage_team(self):
        """Adds a method manage_team()"""
        return f"Managing the {self.department} department."


class Engineer(Employee):
    """Create an Engineer class inherits from Employee"""

    def __init__(self, name, age, employee_id, salary, programming_language):
        """Adds a programming_language attribute"""
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def code(self):
        """Adds a method code()"""
        return f"Coding in {self.programming_language}."


class TechnicalManager(Manager, Engineer):
    """Create a TechnicalManager class that uses multiple inheritance"""

    def __init__(self, name, age, employee_id, salary, department, programming_language):
        """Initialize TechnicalManager"""
        # Initialize the Person part
        Person.__init__(self, name, age)
        # Set all other attributes directly
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
        self.programming_language = programming_language


def show_hierarchy(cls):
    """Takes a class as a parameter and prints the MRO"""
    print(f"Class hierarchy for {cls.__name__}")
    for c in cls.__mro__:
        print(c.__name__)


# Test your implementation
# Create instances
person = Person("John Smith", 30)
employee = Employee("Alice Johnson", 35, "E12345", 60000)
manager = Manager("Bob Williams", 45, "M54321", 85000, "Marketing")
engineer = Engineer("Carol Davis", 28, "E98765", 75000, "Python")
tech_mgr = TechnicalManager("Dave Wilson", 40, "TM24680", 90000, "R&D", "Java")

# Test basic methods
print(person.introduce())
print(employee.introduce())
print(f"Monthly pay: ${employee.calculate_paycheck():.2f}")
print(manager.manage_team())
print(engineer.code())

# Test inheritance hierarchies
print("\nHierarchy demonstrations:")
show_hierarchy(TechnicalManager)

# Test method resolution in multiple inheritance
print("\nTechnical Manager tests:")
print(tech_mgr.introduce())
print(f"Monthly pay: ${tech_mgr.calculate_paycheck():.2f}")
print(tech_mgr.manage_team())
print(tech_mgr.code())
