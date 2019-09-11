import random

RandomNum = random.randint(0,1023)

print ("I'm Thinking of a Number Between 0 and 1023, Can You Guess It?")

while True:
    guess = int(input("Enter Your Guess: ")) 
    if guess == RandomNum:
        print ("Correct, You Guessed it!")
        break
    if guess < RandomNum:
        print ("Your Guess is Too Low!, Try Again.")
        continue
    if guess > RandomNum:
        print ("You Guess is Too High!, Try Again.")
        continue

print ("Congratulations!")

    
