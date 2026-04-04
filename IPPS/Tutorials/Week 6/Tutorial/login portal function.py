def login(uid,pw):
        if uid == "ADMIN" and pw == "StOrE@1":
            print("LOGIN SUCCESSFUL")
            return True
        else:
            print("Wrong Username or Password")
            return False
verified = False
for i in range(1,4):
    user_id = input("enter your user id : ")
    password = input("enter ther password:")    
    verified = login(user_id,password)
    if verified == True:
        breakss
if verified == False:
    print("Account Blocked")
