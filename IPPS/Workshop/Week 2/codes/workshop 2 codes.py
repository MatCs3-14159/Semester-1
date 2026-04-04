#2.1 Write a python program to prompt the user for input number and print square of that particular integer.

"""num=int(input("enter the number: "))
print(f"The square of {num} is {num**2}")"""

#2.2 Write a python program to display the circumference of a circle. (import math module)

"""import math
radius=float(input("Enter the radius of circle:"))
print(f"Circumference = {2*math.pi*radius :,.2f}")"""

#2.3 Write a python program to ask in kilograms and convert into grams.

"""weight=float(input("enter the weight in kilograms: "))
print(f"{weight} kilograms = {weight*1000} grams")"""

#2.4 Write a python program to display the area of the triangle.

"""base=float(input("enter the base measurement of triangle in cm:"))
height=float(input("enter the height measurement of triangle in cm:"))
print(f"The area of triangle is {0.5*base*height} cm\u00B2.")"""

#2.5 Write a python program to prompt user to input their name and display “Hello <<NAME>>”

"""name=input("enter your first name:")
print(f"Hello {name}.")"""

#2.6 Write a python program to print this address as it is.
            # Biratnagar International College,
            # Bhrikuti Marg, Biratnagar
            # Biratnagar, Nepal

"""print("Biratnagar International College, \n Bhrikuti Marg, Biratnagar \n Biratnagar, Nepal")"""

#3.1 Write a python program to find the remainder of a given number if divisor is 2.

"""num=int(input("enter the number: "))
print(f"Remainder of {num} when divisor is 2 is {num%2}")"""

#3.2 Demonstrate the use of “ord()” and “chr()”  functions using a simple python program. [Take Data From User’s]

"""print(f"chr(65)={chr(65)}")
print(f"ord('A')={ord('A')}")

#3.3 Write a python program to calculate BMI of a person when all parameters are provided. BMI= weight(kg)/height(m^2)

weight=float(input("enter the weight in kgs: "))
height=float(input("enter the height in m: "))
print(f"BMI= {weight/(height**2):,.2f}")

#3.4 Write a program to find the cube root of a number. Prompt the user to input a number and print the cube root of the number.

import math

num=int(input("enter the number:"))
print(f"Cube root= {math.cbrt(num):,.2f}")

#3.5 Suppose you are a teacher, and you want to create a program that takes in grades from three exams and calculates the average grade for a student. Develop a program to print out the average marks of a particular student. 

"""grade1=float(input("enter the grade of maths: "))
grade2=float(input("enter the grade of science: "))
grade3=float(input("enter the grade of english: "))
sum=grade1+grade2+grade3
print(f"Average grade= {sum/3:,.2f}")"""

#3.6 Suppose there are 20 students in a class and 8 of them are left-handed. What is the probability of randomly selecting a left-handed student from the class? (Hint: probability = left_handed_students/ total_students).

"""total_std=20
left_handed=8
print(f"Probablity of selecting a left handed student from the class = {left_handed/total_std}")"""

#3.7 A teacher has 50 sheets of paper and wants to distribute them equally among 15 students. How many sheets of paper will each student receive and how many sheets will be left over

"""total_sheets=50
students=15
print(f"Each student will get {50//15} sheets equally and {50%15} sheets will be left over. ")"""

#3.8 A student has a rectangular desk with dimensions of 80 cm by 60 cm. They want to cover the entire desk with a piece of paper. To ensure that the paper covers the desk entirely, the paper must be at least as large as the desk. However, if the paper is much larger than the desk, it may be wasteful. Therefore, we want to find the minimum size of paper needed to cover the desk entirely.

"""length=80
breadth=60
print(f"Minimum size of paper required to cover the desk entirely is {80*60} cm\u00B2.")

#4.1 You’re waiting at a station, and the announcer has just broadcast that your train is going to be 13445 seconds late. You need to work out in understandable terms what that means. You assume this is going to be quite a long time so you whip out your laptop to write a program to convert the seconds into hours, minutes and seconds, aiming to maximize readability by giving priority to the largest units, i.e. the resulting seconds and minute’s values must not be greater than 60.

#You will need four variables to hold: the total number of seconds; the number of hours; the number of minutes; and the number of remaining seconds. The example output should look something like this:
#13445 Seconds is: 3 Hours, 44 Minutes and 5 Seconds.

total_sec=13445
hours=13445//3600
minutes=(13445%3600)//60
seconds=(13445%3600)%60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds.")

#4.2 Write a program to calculate in how many days a work will be completed by three persons A, B and C together. A, B, C take x days, y days and z days respectively to do the job alone. The formula to calculate the number of days if they work together is xyz/(xy + yz + xz) days where x, y, and z are given as input to the program.

x=int(input("enter the number of days person A took to complete the work:"))
y=int(input("enter the number of days person B took to complete the work:"))
z=int(input("enter the number of days person C took to complete the work:"))
print(f"If they work together, total number of days to complete the work is {(x*y*z)/((x*y)+(y*z)+(x*z)):,.2f} ")
