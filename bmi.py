weight = int(input("Enter weight (kg): "))
height = int(input("Enter height (m): "))

bmi = weight / (height * height)


if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal weight")
elif bmi >=29.9:
    print("Overweight")
else:
    print("Obese")





# Questionable