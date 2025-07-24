# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior
# Your code here:

age = int(input("Enter age: "))
if age<=12:
    answer="Child"
if age>=13 and age<=19:
    answer="Teenager"
if age>=20 and age<=59:
    answer=("Adult")
if age>=60:
    answer=("Senior")
print("You are : ",answer)