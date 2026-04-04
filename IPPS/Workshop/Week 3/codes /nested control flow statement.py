age = 20
ticket = True

if age >= 18:  # First condition
    print("You are old enough for entry.")
    
    if ticket:  # Second condition inside the first one
        print("You may enter the movie theater!")
    else:
        print("Sorry, you need a ticket to enter the movie theater.")
else:
    print("You are not allowed to enter as u are below legal age category.")
