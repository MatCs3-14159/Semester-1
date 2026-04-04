name = "Sagar Mishra"
print(name)
#program
people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 16},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 18}
]
adults = [person for person in people if person["age"]>18]
print (adults)
