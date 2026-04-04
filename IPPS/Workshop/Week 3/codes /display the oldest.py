age = []
for i in range (1,5):
    age_person = int (input(f"enter the number of person {i}:"))
    age.append(age_person)
oldest = max(age)
person = age.index(oldest) + 1
print (f"Person {person} is oldest and {oldest} years old.")
