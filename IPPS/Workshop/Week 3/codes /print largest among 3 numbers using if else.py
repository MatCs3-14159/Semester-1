num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))
if num1>num2 or num3>num2:
    if num1>num3:
        print (num1)
    else:
        print (num3)
else:
    print (num2)
