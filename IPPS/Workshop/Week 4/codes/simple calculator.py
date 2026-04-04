while True:
    print("\n--- Simple Calculator ---")
    print("Enter 'q' at any time to quit.")
    num1 = input("Enter first number: ")
    if num1 == "q":
        break
    num2 = input("Enter second number: ")
    if num2 == "q":
        break
    num1 = float(num1)
    num2 = float(num2)
    print("\nChoose an operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    op = input("Enter your operation: ")
    if op == "q":
        break
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            result = "Error: Cannot divide by zero!"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation!"
    print("Result:", result)
print("\nCalculator exited. Goodbye!")
