try:
    amount = float(input("Enter the amount of money: "))
    if amount < 10000:
        raise ValueError("Amount must be at least 10,000")
except ValueError as ve:
    print(f"Error: {ve}")
else:
    print(f"You entered a valid amount: {amount}")
