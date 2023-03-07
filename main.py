import random

#welcomes the user into the game
print("Welcome to Michael's number guessing game")

#makes a variable to store the correct number and generates a number
answer = random.randint(0,10)
userInput = int(input("Guess a number between 1 and 10. "))

#if the input is higher than 10, the program will abuse you for being wrong, and then ask you to try again.
while userInput >= 10:
  userInput = int(input("That is higher than ten you absolute buffoon, I clearly stated that it should between one and ten, did anyone even teach you how to read. I am genuinely impressed at your stupidity, which is impossible since I am a program on a computer that cannot feel emotion, try again loser. "))

#makes a loop for while the input does not equal the answer. when the user inputs the incorrect answer it asks you to try again
while userInput != answer:
  userInput = int(input("Try again "))

print("Good Job, You got it.")