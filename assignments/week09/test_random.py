import random

def test_random():
    random_number = random.randint(1, 21)
    guess = int(input("What is your guess random number:1-20 "))
    
    
    if guess == random_number:
        print("Congratulation you win ♥♥♥")
    else:
        print("You Lose ")
            
    print("Correct number: ",random_number)
    
test_random()