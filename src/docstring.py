def calculate(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: Product of the two numbers.
    """
    return a * b

    #Function docstring
    def greet(name):
    """
    Prints a welcome message.

    Args:
        name (str): Name of the user.

    Returns:
        None
    """
    print(f"Welcome, {name}!")

greet("Pooja")

#Class docstring
class Employee:
    """
    Represents an employee.

    Attributes:
        name (str): Employee name.
        age (int): Employee age.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

employee = Employee("Pooja", 23)

print(employee.name)
print(employee.age)

#Module docstring
class Calculator:

    def multiply(self, x, y):
        """
        Multiplies two numbers.

        Args:
            x (int): First number.
            y (int): Second number.

        Returns:
            int: Product of x and y.
        """
        return x * y

calc = Calculator()

print(calc.multiply(5, 8))

#Method docstring
class Calculator:

    def multiply(self, x, y):
        """
        Multiplies two numbers.

        Args:
            x (int): First number.
            y (int): Second number.

        Returns:
            int: Product of x and y.
        """
        return x * y

calc = Calculator()

print(calc.multiply(5, 8))

#Accessing a docstring
def square(number):
    """
    Returns the square of a number.
    """
    return number ** 2

print(square.__doc__)