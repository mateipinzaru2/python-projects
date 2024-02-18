"""
EMPLOYEE MANAGEMENT
You've recently been hired to work at a new startup, Dev.boot! The company has yet to implement any system for tracking employees within the company. Your manager has assigned you the task!

CHALLENGE
Unfortunately, Dev.boot engineers kinda suck. Rather than creating a Company class that uses instance variables to track employees, they've decided to use an Employee class that uses class variables to track employees.

It's not the cleanest implementation, but you're stuck with it. Hey, at least you get to practice using class variables!

CLASS VARIABLES
Initialize the following class variables:

company_name set to "Dev.boot".
total_employees set to 0.
CONSTRUCTOR
The constructor should take the following parameters (in order) and set them to the corresponding instance variables:

first_name = first_name
last_name = last_name
id = id
position = position
salary = salary
Also, it should increment the total_employees class variable each time a new Employee is created. Remember, total_employees is a class variable, not an instance variable.

GETTER
Add a get_name method that returns the employee's full name as a string (e.g. "John Doe").
"""


class Employee:
    # Initialize class variables
    company_name = "Dev.boot"
    total_employees = 0

    # Constructor
    def __init__(self, first_name, last_name, employee_id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = employee_id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1

    # Getter Method
    def get_name(self):
        return f"{self.first_name} {self.last_name}"
