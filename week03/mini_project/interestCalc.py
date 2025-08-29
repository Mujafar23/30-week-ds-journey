principle = int(input("Enter the principle: "))
rate = int(input("Enter the rate: (%) "))
time = int(input("Enter the time: (years) "))
interest = principle * rate * time / 100
total = principle + interest
print(f"The interest is: {interest}")
print(f"The total is: {total}")