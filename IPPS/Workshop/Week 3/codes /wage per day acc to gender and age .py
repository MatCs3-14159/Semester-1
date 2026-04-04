age = int (input ("enter your age:"))
gender = input("M for male \n F for female \n enter your gender:")
days = int (input ("Number of days you worked:"))
if age>=18 and age<30:
    if gender == "M":
        print (f"Wage = {700 * days}")
    else:
        print (f"Wage = {750 * days}")
elif age>=0 and age<=40:
        if gender == "M":
            print (f"Wage = {800 * days}")
        else:
            print (f"Wage = {850 * days}")
else:
    print ("Not valid!")
    
