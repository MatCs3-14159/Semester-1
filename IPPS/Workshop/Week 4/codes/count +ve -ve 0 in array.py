inp = []
count_positive = 0
count_negative = 0
count_zero = 0
while True:
    n = input ("Enter the number:")
    try:
        inp.append(int (n))
    except:
        break
for n in inp:
    if n < 0:
        count_negative += 1
    elif n > 0:
        count_positive += 1
    else:
        count_zero +=1
print (f"Your input = {inp} ⬇️\n Positive numbers = {count_positive}\n Negative numbers = {count_negative}\n Zeros = {count_zero}")
        
