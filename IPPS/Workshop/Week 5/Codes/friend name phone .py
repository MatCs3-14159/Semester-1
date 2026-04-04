name = "Sagar Mishra"
print(name)
#program
friends = {}
n = int (input ("enter the number of friends you want to add: "))
for i in range(n):
    name = input (f"enter the name of {i+1}th friend: ")
    phn_num =  input (f"enter the phone number of {i+1}th friend: ")
    friends[name] = phn_num
    
#A. Display all friends
print (f"\n All friends and their phone numbers: ")
for name,phn_num in friends.items():
    print (f"{name}: {phn_num}")

#B. Add a new friend
new_name = input ("enter the name of friend: ")
new_phn_num = input ("enter the phone number: ")
friends[new_name] = new_phn_num
print ("\nDictionary after adding new friend:")
print (friends)

#C. Delete a particular friend
del_name = input("\nEnter the name of the friend to delete: ")
if del_name in friends:
    del friends[del_name]
    print(f"\nDictionary after deleting {del_name}:")
    print(friends)
else:
    print(f"{del_name} not found in the dictionary.")

#D. Modify the phone number of an existing friend
mod_name = input("\nEnter the name of the friend whose number you want to modify: ")
if mod_name in friends:
    new_number = input(f"Enter the new phone number of {mod_name}: ")
    friends[mod_name] = new_number
    print(f"\nDictionary after modifying phone number:")
    print(friends)
else:
    print(f"{mod_name} not found in the dictionary.")

#E. Check if a friend is present and display sorted dictionary
check_name = input("\nEnter the name of the friend to check: ")
if check_name in friends:
    print(f"{check_name} is present with phone number {friends[check_name]}")
else:
    print(f"{check_name} is not present in the dictionary.")

# Display dictionary sorted by friend names
print("\nDictionary in sorted order by names:")
for name in sorted(friends.keys()):
    print(f"{name}: {friends[name]}")

