import random

randorator = random.randint(1,99)
attempts = 0
userchoice = 0


print("This is an interactive guessing game!\n You have to enter a number between 1 and 99 to find out the secret number.\n Type 'exit' to end the game.\n Good luck!")

while True : 
    attempts = attempts + 1
    userchoice = input ("What's your guess between 1 and 99?\n") 
    if userchoice == 'exit' :
        print("Goodbye!")
        break 
    userchoice = int(userchoice)
    if userchoice < randorator :
        print("Too low!")
    elif userchoice > randorator :
        print("Too high!")
    elif userchoice == randorator and randorator == 42 :
        print('The answer to the ultimate question of life, the universe and everything is 42.')
    elif attempts == 1  :
        print("Congratulations! You got it on your first try!")
        break 
    else :
        print("Congratulations, you've got it!\nYou won in " + str(attempts) + " attempts!")
        break
