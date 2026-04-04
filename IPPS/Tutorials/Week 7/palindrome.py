a = input("Enter the string:")
if a == a[::-1]:
    print (f"Palindrome : {a} and {a[::-1]}")
else:
    print (f"Not a Palindrome : {a} and {a[::-1]}")
