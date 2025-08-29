weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi} ({category})")