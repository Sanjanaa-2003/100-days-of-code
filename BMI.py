height = input("Enter height is metres:\n")
weight = input("Enter weight is kg:\n")
height_in_metres=float(height)
weight_in_kg=int(weight)
BMI=weight_in_kg/height_in_metres**2
print(int(BMI))
if BMI<18.5:
    print("You are underweight!:(")
elif BMI>=18.5 and BMI<=24.9:
    print("You are healthy!:)")
else:
    print("You are overweight")