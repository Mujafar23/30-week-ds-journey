for i in range(10):
    print(i)
for i in range(1, 6):
    print(i)

str1 = "Hello this is a string"
for char in str1:
    print(char)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    print(num)

#Write a program that uses a `for` loop to calculate the sum of all numbers from 1 to 10.
total =0
for i in range(1, 11):
    total +=i
    print(f"The sum of {i} is {total}")

#printing even numbers
for i in range(2, 22, 2):
    print(i)
#reverse a string
my_string = "Python"
reversed_string = ""
for char in my_string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)

# List Comprehension
for i in range(1, 11):
    print(i**2)

squares = [n**2 for n in range(1, 11)]
print(squares)

#while loop
count = 0
while count < 5:
  print(count)
  if count == 3:
    break  # Exit the loop when count is 3
  count += 1
print("Loop finished.")

#Number Guessing Game:**
# *   Generate a random number between 1 and 10 (inclusive).
# *   Prompt the user to guess the number.
# *   Use a `while` loop to keep asking for guesses until the user guesses correctly.
# *   Provide feedback to the user (e.g., "Too high", "Too low").
import random
secrec_nymber = random.randint(1, 10)
guess = 0
while guess != secrec_nymber:
    guess = int(input("Guess: "))
    if guess < secrec_nymber:
        print("Too low.")
    elif guess > secrec_nymber:
        print("Too high.")
    else:
        print("Correct!")

#sum of numbers
num = int(input("Enter a number: "))
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print(f"The sum of {num} is {total}")

#countdown
start_num = int(input("Enter a starting point: "))
i = start_num
while i <= 1:
    print(i)
    i -=1


