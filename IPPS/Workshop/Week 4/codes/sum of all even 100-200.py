sum = 0
i = 100
while True:
    if i>=100 and i<=200:
        sum += i
    elif i<100 or i>200:
        break
    else:
        continue
    i+=2
print (sum)
