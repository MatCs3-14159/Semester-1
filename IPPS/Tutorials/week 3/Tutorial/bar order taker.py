drink=int(input("1 for alcoholic \n 2 for non-alcoholic. \n enter your order: "))
if drink==1:
    age=int(input("Check ID \n check age= "))
    if age>17:
        serve=input("Your age is legal for drinking alcoholic drink. \n enter your drink name:")
        print(f"Your {serve} will be ready soon. Please wait!")
    else:
        print("You can't order alcoholic drink as per law.")
elif drink==2:
    serve=input("enter your drink name:")
    print(f"Your {serve} will be ready soon. Please wait!")
else:
    print("Do u want any bevrage?")
    
