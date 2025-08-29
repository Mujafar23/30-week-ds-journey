num1 = int (input("enter first number: "))
num2 = int (input("enter second number: "))

operator = input("enter operator: ")
if operator == '+':
    result = num1 + num2
    print(f"result: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"result: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"result: {result}")
elif operator == '/':
    result = num1 / num2
    print(f"result: {result}")