weight = float(input("enter the weight in kilograms:"))
height = float(input("enter the height in centimeters:"))
height = height/100
BMI = weight/(height**2)
print (f"{BMI:,.2f}")
if BMI<18.5:
    print ("Underweight")
elif BMI < 25:
    print ("Normal weight")
elif BMI < 30 :
    print ("Overweight")
else:
    print ("Obese.")
    
