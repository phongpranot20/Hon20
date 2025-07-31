"""
Personal Information Manager 
#Phongpranot Boonmak 6730251174
#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person 
    person = ("Phongpranot", 20, "Chonburi", "Thai")  # name, age, city, country
    hobbies = []
    
    while True:
        print("\n=== Personal Info Manager ===")
        print("1. Display info")
        print("2. Add hobby")
        print("3. Remove hobby")
        print("4. Edit age")
        print("5. Exit")
        
        choice = input("What do you want to do?: ")
        
        if choice == "1":
            print("\n--- Info ---")
            print("Name:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hobbies:", hobbies if hobbies else "None")

        elif choice == "2":       
            hobby = input("Insert new hobby: ")
            hobbies.append(hobby)
            print(f"Hobby '{hobby}' added!")

        elif choice == "3":
            if hobbies:
                print("Current hobbies:", hobbies)
                to_remove = input("Which hobby do you want to remove?: ")
                if to_remove in hobbies:
                    hobbies.remove(to_remove)
                    print(f"Hobby '{to_remove}' removed!")
                else:
                    print("Hobby not found.")
            else:
                print("No hobbies to remove.")

        elif choice == "4":
            try:
                age = int(input("Insert new age: "))
                person_list = list(person)
                person_list[1] = age
                person = tuple(person_list)
                print("Age updated.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    personal_info_manager()
