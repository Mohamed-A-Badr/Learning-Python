import random
import string

typeOfGame = 0
while True:
    try:
        print("Which game you want:")
        print("1- Guessing number")
        print("2- guessing character")
        typeOfGame = int(input("Enter your choose's number:"))
    except ValueError:
        print("Enter a valid choose")
    if typeOfGame >= 1 and typeOfGame <= 2:
        break
    else:
        print("Wrong choice, try again")

if typeOfGame == 1:
    try:
        start = int(input("Choose your start range: "))
        end = int(input("Choose your end range: "))
        correctNumber = random.randint(start, end)
        while True:
            guess = int(input("Enter your guess: "))
            if guess == correctNumber:
                print("Congrat, You're Right")
                break
            else:
                print("You'r Wrong try again")
    except ValueError as err:
        print("Please Enter valid integer number")

elif typeOfGame == 2:
    correctCharacter = random.choice(string.ascii_letters)
    while True:
        guess = input("Enter your guess: ").lower()
        if guess == correctCharacter:
            print("Congrat, You're right")
            break
        else:
            print("Worng, try again")
