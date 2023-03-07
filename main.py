import random

#welcomes the user into the game
print("Welcome to Michael's number guessing game")

#makes a variable to store the correct number and generates a number
answer = random.randint(0,10)
userInput = int(input("Guess a number between 1 and 10. "))


#makes a loop for while the input does not equal the answer. when the user inputs the incorrect answer it asks you to try again
while userInput != answer:
  userInput = int(input("Try again "))

print("Good Job, You got it.")