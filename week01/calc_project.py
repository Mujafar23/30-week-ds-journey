from random import choice

print("Calculator")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("""
Choices are:
    Addition for press 1
    Subtraction for press 2
    Multiplication for press 3
    Division for press 4
""")
choice = int(input("Enter choice: "))
if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(subtract(num1, num2))
elif choice == 3:
    print(multiply(num1, num2))
elif choice == 4:
    print(divide(num1, num2))
else:
    print("Invalid choice")


