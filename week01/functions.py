"""Function
"""
def func1(a, b):
    """ It returns addition of two numbers """
    return a + b
print(func1(1, 2))

def greet(name):
    """
    Greets a person by name.

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return "Hello, " + name + "!"
print(greet("John"))

#A function to calculate the square of a number
def square(number):
    """
    Calculates the square of a number.

    Parameters:
        number (int or float): The number to square.

    Returns:
        int or float: The square of the number.
    """
    return number * number
print(square(5))

# 3. A function to check if a number is even
def is_even(number):
    """
    Checks if a number is even.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0
print(is_even(76))

def greets(name, greetig = "Welcome"):
    return greetig + ", " + name
print(greets("Muzaffar"))


def calculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(calculate_sum(1, 2, 3))  # Output: 6
print(calculate_sum(10, 20, 30, 40, 73, 583, 2))


def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_details(name="Eve", age=25, city="London")


def square(x):
    return x * x
def cube(x):
    return x * x * x


operational_list = [2, 3, 23, 3, 2, 5]
result_list = []
def process_data(numbers, operation):
    for numbers in operational_list:
        result_list.append(operation(numbers))

print(process_data(operational_list, cube))
print(operational_list)
print(result_list)

given_list = ["welcome its our world"]
output_list = []
def up(s):
    return s.upper()

def down(s):
    return s.lower()

def opr(ls, op):
    for item in ls:
        output_list.append(op(item))
print(opr(given_list, up))

print(given_list)
print(output_list)
