num = int (input ("enter the number:"))
if num%3==0 and num%5==0:
    print ("FizzBuzz")
elif num%3==0:
    print ("Fizz")
elif num%5==0:
    print ("Buzz")
else:
    print ("not divisible by 3 or 5")
