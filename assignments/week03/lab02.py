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
        if choice == "1":
           print("Your balance is:", balance)
        elif choice == "2":
           amount = int(input("Enter amount to withdraw: "))
           if amount > balance:
               print("Insufficient funds.")
           else:
               balance -= amount
               print("Withdrawal successful. New balance is:", balance)
        elif choice == "3":
           amount = int(input("Enter amount to deposit: "))
           balance += amount
           print("Deposit successful. New balance is:", balance)
        elif choice == "4":
           print("Thank you for using our ATM. Goodbye!")
           break
        else:
           print("Invalid option.")
else:
    print("Invalid PIN")