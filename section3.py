#section 3
# stretch challenge (BMI Calculator)
name = input("Enter your name :")
weight = float(input("Enter your weight in kg :"))
height = float(input("Enter your height in meters :"))
BMI = weight/height**2
print("Your BMI is :",BMI)
if BMI < 18.5 :
    print("Underweight")
elif BMI <25 and BMI >18.5 :
    print("Normal")
else:
    print("Overweight")






