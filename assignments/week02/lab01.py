#BMI Calculator (20 points)

#Write a program that:

#Asks for height in meters
#Calculates BMI using formula: BMI = weight / (height²)
#Displays BMI with 1 decimal place
#Shows BMI category based on the ranges below

#BMI Categories:

#0 and above: Obese

#***


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