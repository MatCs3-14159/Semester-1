print ("Sagar Mishra")
#peogram
print("Calculator Program with Docstrings")

def add(a, b):
    """
    Adds two decimal numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second decimal number from the first.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two decimal numbers.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divides the first decimal number by the second.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float or str: Quotient of a and b, or error message if b is zero
    """
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


def modulus(a, b):
    """
    Finds the remainder when the first decimal number is divided by the second.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float or str: Remainder or error message if b is zero
    """
    if b != 0:
        return a % b
    else:
        return "Cannot perform modulus by zero"


def exponent(a, b):
    """
    Raises the first decimal number to the power of the second.

    Parameters:
    a (float): Base number
    b (float): Exponent

    Returns:
    float: Result of a raised to power b
    """
    return a ** b


# Using help() to check docstrings
help(add)
help(subtract)
help(multiply)
help(divide)
help(modulus)
help(exponent)
