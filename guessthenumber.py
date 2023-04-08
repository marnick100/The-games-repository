import random

print("Guess the Number Game")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it in 10 tries or less?")

number = random.randint(1, 100)
tries = 0

while tries < 10:
    guess = int(input("Take a guess: "))
    tries += 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number in", tries, "tries.")
        break

if tries == 10:
    print("Sorry, you ran out of tries. The number was", number)
