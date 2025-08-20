
#BMI Categories:

#20.5 - 25.9: Normal weight
#26.0 - 30.9: Overweight
#31.0 and above: Obese

60


weight = float(input("Weight: "))
height = float(input("Height: "))
bmi = weight / height ** 2
print("Your BMI: ", bmi)
if bmi < 19.5:
    print("Underweight")
 
if bmi >= 20.5 and bmi <= 25.9:
    print("Normal Weight")
if bmi >= 26.0 and bmi <= 30.9:
    print("Overweight Weight")
if bmi >=31.0:
    print("Obese")