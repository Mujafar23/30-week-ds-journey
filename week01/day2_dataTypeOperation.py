#Numeric types
#integer(int) Whole numbers 5, -12, 10000
i = 2
#Floating-point numbers(float) 3.14, -0.32, 2.3
f = 3.14
#Complex numbers (complex) 3+4j, 2j, 2-12j
c = 46+2j
#Arithmetic operations
2+3
5-2
3*2
13/2
12//3
13%6
2**3

#practice problems
print(15%4)
#3
print(9//2)
#4
print(2**5)
#32
print(3+4.0)
#7.0
#Write an expression that calculate area of circle
r = 5
pi = 3.14
a = pi*r**2
print(a)
#Evaluate
print(((10+2)*3)**2//6)

print(4+3j+2-5j)
#python program to check if a number is even or odd
a=23
if a%2==0:
    print("its even")
else:
    print("its odd")

#program to convert the temperature from Celsius to Fahrenheit
Ce = 23
Fe = (Ce * 9/5) + 32
print(Fe)
#String
string1 = 'Hello'
string2 = "World"
string3 = """
Hello I am
Here
"""
#String indexing
my_string = "Python is awesome"
print(my_string[0])
print(my_string[7])
print(my_string[3:5])
print(my_string[-7])

#sting slicing
n = "Programming"
print(n[0:4])
print(n[5:])
print(n[:6])
print(n[::2])
print(n[::-1])

#string methods
str1 = "Hello world"
str2 = "Python is awesome"
print(str1.upper())
print(str2.upper())
print(str1.lower())
print(str2.lower())
print(str1.strip())

print(str2.replace("Python", "JavaScript"))
print(str2.replace("H", ""))
print(str2.capitalize())
print(str2.title())
print(str2.isupper())
print(str2.islower())

#multiple methods
print(str2.strip().upper())

#logical operators
is_valid = True
print(is_valid)
is_clear = False
print(is_clear)

age =23
is_adult = age >= 18
print(is_adult)
name = "Hero"
is_name_empty = len(name) == 0
print(is_name_empty)

#logical operators and or not
#example
x = 5
y = 13
is_greater_than = x > y
is_less_than = x < y
print(is_less_than)
print(is_greater_than)

is_raining = True
is_sunny = False

is_cloudy = is_raining and is_sunny
print(is_cloudy)

#none value
my_variable = None
print()
# Use `is None` for proper checking:

if my_variable is None:
    print("my_variable is None")
else:
    print("my_variable has a value.")

#string formatting
name = "Hero"
age = 23
print(f"Hello, {name}! You are {age} years old.")
price = 99.456
print(f"Price: ${price:.2f}")
Firstname = input("Enter your name: ")  # Returns a string
ageS = int(input("Enter your age: "))  # Convert to integer
print("Name:", Firstname, "Age:", ageS)
print(f"{name = }, {age = }")
#mini project
Name2 = input("Enter your name: ")
doe = int(input("Enter your date of birth year: "))
current_year = 2025
age2 = current_year - doe
print(f"Your name is{Name2 = },and your is {age2 = } according to Date of year")