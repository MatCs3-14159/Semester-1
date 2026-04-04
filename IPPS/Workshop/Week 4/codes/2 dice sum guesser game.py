import random
print("🎲 Welcome to the Dice Guessing Game!")
print("Enter 'q' to quit anytime.\n")
while True:
    guess = input("Guess the total of two dice (2–12): ")
    if guess == "q":
        break
    guess = int(guess)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"\nDice rolled: {dice1} and {dice2}")
    print(f"Total: {total}")
    if guess == total:
        print("🎉 Correct! You guessed the total!")
    else:
        print("❌ Wrong guess! Try again.")
    print("\n--- Next Round ---\n")
print("\nGame Over! Thanks for playing! 🎲")
