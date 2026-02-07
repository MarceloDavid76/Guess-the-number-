import random
from art import logo

print(logo)
print("Welcome to the Number Guessisng Game")
print("I'am thinkink a number between 1 to 100 ")
choice = random.randint(1, 100)
print(choice)
difficultY = input("Choose a difficult. Type 'easy' or 'hard ")

if difficultY == "easy":
    attempt = 10
else:
    attempt = 5

def check(x, y):
    if(x > y):
        print("too low")
        print()

    else:
        print("too high")
        print()


while attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number ")
    attempt -= 1
    guess = int(input("Make a guess: "))
    if guess == choice:
        print(f"You got it! Yhe number was {choice}")
        break
    elif attempt == 0:
        print("You've run out of guesses, you lose!")
    else:
        check(x= choice, y= guess)



        




