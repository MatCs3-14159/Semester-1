name = "Sagar Mishra"
print(name)
#program
n = int (input ("length of list:"))
a = []
for i in range (n):
    x = int (input (f"enter the {i+1}th number: "))
    if x <= 100:
        a.append(x)
    else:
        a.append("over")
print(a)
