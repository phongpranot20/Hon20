"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

import random

def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    # Return narrowed range around the number
    return f"HINT: The narrowed range  + {range(current_min, current_max)}"

def get_thefirst_digit_hint(number):
    # Retun the first digit of the number
    return f"HINT: The first digit of number is {number //10}"


def test_random():
    random_number = random.randint(1, 101)
    print("=== Enhanced GUESSING GAME ===")
    i = 0 

    while True:
     
     print(f"Attempt {i+1}")
     guess = int(input("Guess my number between 1-100 : ")) 
     if guess == random_number:
        print("Congratulation you win ♥♥♥")
        print("Correct number: ",random_number)
        
     elif guess < random_number:
        print("Too Low")
     elif guess > random_number:
        print("Too High")

     if i == 3:
        print(get_parity_hint(random_number))
     elif i == 5:
        print(get_divisibility_hint(random_number))
     elif i == 7:
        print(get_range_hint(random_number, random_number-12 , random_number+12))
     elif i == 10:
        print (get_thefirst_digit_hint(random_number) )   
     i = i +1    

test_random()
