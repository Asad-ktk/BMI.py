weight=float(input("Enter your weight please: "))
height=float(input("Enter your height please (in meters): "))
bmi = weight / ( height ** 2 )
if (bmi < 18.5 ):
    print("Underweight")
elif (bmi > 30):
    print("Obese")
elif (bmi < 25 ):
    print("Perfect")
else:
    print("Overweight")