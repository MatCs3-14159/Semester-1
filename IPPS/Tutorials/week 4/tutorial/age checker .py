valid_input = True
while valid_input:
    age=int(input("enter your age:"))
    if age<0:
        print(f"Invalid input!!.. Are u really {age} years old.")
    else:
        valid_input = False
print(f"Your age is {age}.")
