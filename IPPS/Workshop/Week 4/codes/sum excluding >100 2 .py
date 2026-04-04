sum = 0

while True:
    n = int (input ("Enter number (Space to end): "))
    if n<100:
        sum += int(n)
        n = input ("Enter number (Space to end): ")
    else:
        break 
print(sum)
