# age = 12
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

marks = 78
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

#Nested if
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("Id required")
else:
    print("Access denied")

#🧠 Practice Problems
#Q1. Check if a number is positive, negative, or zero.
num = -3
if num == 0:
    print("number is 0")
elif num < 0:
    print("number is negative")
elif 0 < num:
    print("number is positive")

#Q2. Write a program to check whether a person is a child (0–12), teenager (13–17), adult (18–59), or senior (60+).
personAge = 45
if  0 < personAge <= 12:
    print("Person is child ")
elif 13 < personAge <=17:
    print("Person is  teenager")
elif 18 < personAge <= 59:
    print("Person is adult")
elif 59 < personAge <=100:
    print("Person is older ")

#Password checker
# password = input("Password: ")
# if password == "acetata":
#     print("access granted")
# else:
#     print("access denied")

# Q4. Take two numbers from the user and:
# If both are positive, print "Both positive"
# If one is positive, print "One positive"
# If both are negative, print "Both negative"
# If either is zero, print "Zero included"
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
elif num1 < 0 and num2 < 0:
    print("Both numbers are negative")
else:
    print("any one is positive")



