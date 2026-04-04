n = int (input ("Enter the number:"))
largest = 0
print (f"largest digit in {n} =", end = " ")
while n > 0:
    digit = n %10
    if largest < digit:
        largest = digit
    n //= 10
print (largest)
