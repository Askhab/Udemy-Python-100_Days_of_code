# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import choice

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guessed_number = choice(range(1, 101))
print(f"Pssst, the correct answer is {guessed_number}")
difficulty_modes = {
    "easy": 10,
    "hard": 5,
}
guesses = difficulty_modes[input("Choose a difficulty. Type 'easy' or 'hard': ")]
print(f"You have {guesses} attempts remaining to guess the number.")
number_guessed = False

while not number_guessed:
    user_guess = int(input("Make a guess: "))

    if user_guess > guessed_number:
        guesses -= 1
        print("Too high.")
    elif user_guess < guessed_number:
        guesses -= 1
        print("Too low.")
    elif user_guess == guessed_number:
        number_guessed = True
        print(f"You got it! The answer was {guessed_number}")
        break

    if guesses != 0:
        print("Guess again")
        print(f"You have {guesses} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses, you lose.")
        break
