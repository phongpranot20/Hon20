# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior
# Your code here:

# Complete this ATM simulation

balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
          print("Thank you to use our ATM")
          break

        if choice == "1":
            print("Now ,you have: ",balance)

        if choice == "2":
            withdraw = float(input("withdraw amount:"))
            balance = balance - withdraw
            print("Now, you have: ",balance)

        if choice =="3":
            deposit = float(input("Deposit amount: "))
            balance = balance + deposit
            print ("Now, you have: ",balance)

else:
    print("Invalid PIN")
