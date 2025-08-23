str = "Python is great programming language"
strUpper = str.upper
print(strUpper)

strL = str.lower
print(strL)

strCapitalize = str.capitalize
print(strCapitalize)

print(str.title())

#cleaning methods
nwstr = "    You are not alone    "
striped_str = nwstr.strip()
print(striped_str)

leftsripped_str = striped_str.lstrip()
print(leftsripped_str)

rightsripped_str = leftsripped_str.rstrip()
print(rightsripped_str)

#search methods
searchstr = "Python is great programming language"
print(searchstr)
print(searchstr.index("great"))
print(searchstr.find("python"))

print(searchstr.startswith("python"))
print(searchstr.endswith("language"))

print(searchstr.__contains__("language"))

my_string = "apple,banana,orange"
fruits = my_string.split(",")  # Split by comma
print(fruits)  # Output: ['apple', 'banana', 'orange']

my_string = "apple,banana;orange|grape"
fruits = my_string.split("[,;|]", 1)  #Split by comma, semicolon, or pipe, but only split once.
print(fruits)  # Output: ['apple', 'banana', 'orange']

fruits = ['apple', 'banana', 'orange']
my_string = ", ".join(fruits)  # Join with ", " as the delimiter
print(my_string)  # Output: apple, banana, orange

fruits = ['apple', 'banana', 'orange']
my_string = "\n".join(fruits)  # Join with newline character
print(my_string)  # Output: apple\nbanana\norange

csv_string = "John,Doe,30,New York"
fields = csv_string.split(",")  # Split by comma
print(fields)  # Output: ['John', 'Doe', '30', 'New York']

# You can then access the individual fields by index:
name = fields[0]
age = fields[2]
print(f"Name: {name}, Age: {age}") # Output: Name: John, Age: 30

data_string = "apple;banana;orange"
fruits = data_string.split(";")
print(fruits)


