sum = 0
s = int (input ("Series length:"))
for i in range(0, s):
    n = int(input("Enter number:"))
    if n<100:
        sum += n
print(sum)
