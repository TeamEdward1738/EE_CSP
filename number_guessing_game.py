# EE, number guessing game

import random

# Secret number range: 1 to 100
secret_number = random.randint(1, 100)

# Player gets 7 attempts
max_attempts = 7

guesses_used = 0

print("Guess the secret number between 1 and 100!")

for attempt in range(max_attempts):
    guess = int(input("Enter your guess: "))
    guesses_used += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct!")
        print("You guessed it in", guesses_used, "guesses.")
        break
else:
    print("You ran out of attempts!")
    print("The secret number was", secret_number)
    print("You lost!")
