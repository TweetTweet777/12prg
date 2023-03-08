print("Guess the hidden number between 1 and 100.")
answer = 52
guess = int(input("Enter your guess."))

while not guess == answer:
    if guess < 1 or guess > 100:
        print("Your guess was not valid. Enter it again.")
    elif guess < answer:
        print("Your guess is too low. Try again.")
    elif guess > answer:
        print("Your guess is too high. Try again.")
    guess = int(input())

print("Correct! Well Done.")