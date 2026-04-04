name = "Sagar Mishra"
print(name)
#program
students = [
    {"student_id": 1, "name": "Jean Castro", "class": "V"},
    {"student_id": 2, "name": "Lula Powell", "class": "V"},
    {"student_id": 3, "name": "Brian Howell", "class": "VI"}, 
    {"student_id": 4, "name": "Lynne Foster", "class": "VI"}, 
    {"student_id": 5, "name": "Zachary Simon", "class": "VII"}
]
def check_key_value(key, value, dict_list):
    for d in dict_list:
        if key in d and d[key] == value:
            return True
    return False
checks = [
    ('name', 'Jean Castro'),
    ('address', 'New York')
]
for key, value in checks:
    if check_key_value(key, value, students):
        print(f"Key: '{key}' and Value: '{value}' do exist.")
    else:
        print(f"Key: '{key}' and Value: '{value}' do not exist.")
