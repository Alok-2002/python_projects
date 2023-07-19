import random

number = random.randint(1, 100)


print("Guess a number between 1 and 100:")
guess = int(input())


while guess != number:
    if guess < number:
        print("Too low! Guess again:")
        guess = int(input())
    else:
        print("Too high! Guess again:")
        guess = int(input())


print("Congratulations, you guessed the number!")
