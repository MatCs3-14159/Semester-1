def check_index(email):
    email_addr = email.find("@")
    print("Index of @ character in the given email address is", email_addr)
email_address = input("Enter your email adddress: ")
check_index(email_address)
