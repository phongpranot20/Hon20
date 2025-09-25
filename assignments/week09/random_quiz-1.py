"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random

def test_random():
    random_number = random.randint(1, 21)
    print("=== SIMPLE GUESSING GAME ===")
    for i in range(6):
     
     print(f"Attempt {i+1}")
     guess = int(input("Guess my number between 1-20 : "))
     if guess == random_number:
        print("Congratulation you win ♥♥♥")
        print("Correct number: ",random_number)
        break
     elif guess < random_number:
        print("Too Low")
     elif guess > random_number:
        print("Too High")

    
test_random()
