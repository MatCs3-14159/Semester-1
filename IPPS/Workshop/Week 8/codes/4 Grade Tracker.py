students = []     
grades_dict = {}   

while True:
    try:
        num_students = int(input("Enter number of students: "))
        if num_students <= 0:
            print("Number of students must be greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

# Input student details
for i in range(num_students):
    name = input(f"\nEnter name of student {i + 1}: ")
    students.append(name)

    while True:
        grade_input = input(f"Enter grades for {name} (separated by commas): ")
        grade_list = grade_input.split(",")

        valid_grades = []
        try:
            for grade in grade_list:
                grade = float(grade.strip())

                if grade < 0 or grade > 100:
                    raise ValueError("Grade out of range")

                valid_grades.append(grade)

            grades_dict[name] = valid_grades
            break

        except ValueError:
            print("Invalid grade detected! Please enter numbers between 0 and 100.")

total_sum = 0
total_count = 0

for grade_values in grades_dict.values():
    total_sum += sum(grade_values)
    total_count += len(grade_values)

class_average = total_sum / total_count
print("\nStudent Grades:")
for student in students:
    print(f"{student}: {grades_dict[student]}")

print(f"\nClass Average Grade: {class_average:.2f}")
