name = "Sagar Mishra"
print(name)
#program
students = [
    {"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
    {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
    {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
    {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
    {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}
]
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}: {average}")
