import random
print("🎲 Welcome to the Dice Guessing Game!")
print("Enter 'q' anytime to quit.\n")
rounds = 0
wins = 0
while True:
    guess = input("Guess the total of two dice (2–12): ")
    if guess == "q":
        break
    guess = int(guess)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    rounds += 1   
    print(f"\nDice rolled: {dice1} and {dice2}")
    print(f"Total: {total}")
    if guess == total:
        wins += 1
        print("🎉 Correct! You guessed the total!")
    else:
        print("❌ Wrong guess!")
    win_percentage = (wins / rounds) * 100
    print(f"\nRounds played: {rounds}")
    print(f"Win percentage: {win_percentage:.2f}%")
    print("\n--- Next Round ---\n")
print("\nGame Over! Thanks for playing! 🎲")
