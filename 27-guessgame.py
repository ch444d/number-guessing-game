import random

low = 1
high = random.randint(low, 1000)
number = random.randint(low, high)
guesses = 0

# print(number)
# print(low)
# print(high)

player_guess = int(input(f"Enter a guess between {low} and {high}: (whole number)"))

while player_guess != number:
    if player_guess > number:
        print("Too high, guess again.")
        guesses += 1
        player_guess = int(input(f"Enter a guess between {low} and {high}: (whole number)"))
    if player_guess < number:
        print("Too low, guess again.")
        guesses += 1
        player_guess = int(input(f"Enter a guess between {low} and {high}: (whole number)"))

if player_guess == number:
    print("Congrats, you win!")
    guesses += 1
    print(f"You guessed {guesses} time(s).")