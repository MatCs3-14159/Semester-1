unit = int(input("Enter the number of electric units consumed: "))
bill = 0
if unit <= 100:
    bill = 0
elif unit <= 300:
    bill = (unit - 100) * 2
else:
    bill = (200 * 2) + ((unit - 300) * 5)
print(f"Total electricity bill is: Rs.{bill}")
