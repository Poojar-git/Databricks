#1. Use 4 Spaces for Indentation
def greet():
    print("Hello")

greet()

#2. Use snake_case for Variables and Functions
employee_name = "Pooja"

def calculate_salary():
    pass

#3. Use PascalCase for Classes
class Employee:
    pass

#4. Use UPPER_CASE for Constants
MAX_SALARY = 50000

print(MAX_SALARY)

#5. Add Spaces Around Operators
x = 10
y = 20
z = x + y

print(z)

#6. Leave Blank Lines Between Functions
def add():
    pass


def subtract():
    pass

#7. Keep Line Length Reasonable(79)
message = (
    "This is a very very very very very very very "
    "very long sentence."
)

print(message)

#8. Import Statements at the Top
import math

print(math.sqrt(25))

#9. Use Meaningful Variable Names
employee_salary = 100
bonus_percentage = 20

#10. Write Docstrings
def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of the two numbers.
    """
    return a * b

print(multiply(5, 4))