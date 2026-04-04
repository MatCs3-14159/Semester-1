import random
secret = random.randint(1, 20)
guesses = []
print("I have selected a number between 1 and 20.")
print("You have 5 chances to guess it!")
for i in range(5):
    guess = int(input(f"Guess {i + 1}: "))
    guesses.append(guess)
    if guess == secret:
        print("🎉 Congratulations! You guessed the number correctly!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print("\n❌ You've used all your guesses!")
    print("The number was:", secret)
    print("Your guesses were:", guesses)
