<<<<<<< HEAD
#BMI Calculator (20 points)

#Write a program that:

#Asks for height in meters
#Calculates BMI using formula: BMI = weight / (height²)
#Displays BMI with 1 decimal place
#Shows BMI category based on the ranges below

#BMI Categories:

#0 and above: Obese

#***
=======

#BMI Categories:

#20.5 - 25.9: Normal weight
#26.0 - 30.9: Overweight
#31.0 and above: Obese

60
>>>>>>> e388efe3fb592e97d92a426e1cf39eda2d50e284


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