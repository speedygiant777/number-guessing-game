import random

gameEntry = input("Would you like to play the Number guessing game? Yes or No?: ").capitalize()
if gameEntry == "No":
    print("Okay come soon!")
    exit()
else:
    pass

guessInt = random.randint(0, 100)

guessNum = int(input("Enter a random number to guess! Hint its a number between 0 and 100: "))

if abs(guessNum - guessInt) <= 10:
    print(f"Computer input: {guessInt}, Your input: {guessNum}, so you win!! ")
else:
    print(f"Computer input: {guessInt}, Your input: {guessNum}, so you loose!!")