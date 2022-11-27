# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi_number = round(weight / height ** 2)

if bmi_number <= 18.5:
    print(f"Your BMI is {bmi_number}, you are underweight.")
elif bmi_number < 25:
    print(f"Your BMI is {bmi_number}, you have a normal weight.")
elif bmi_number < 30:
    print(f"Your BMI is {bmi_number}, you are slightly overweight.")
elif bmi_number < 35:
    print(f"Your BMI is {bmi_number}, you are obese.")
else:
    print(f"Your BMI is {bmi_number}, you are clinically obese.")
