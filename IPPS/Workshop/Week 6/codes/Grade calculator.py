print("Sagar Mishra")
#program
print ("📝GRADE CALCULATOR PROGRAM📝")
#function that calculates percentage and total marks
def grade(modules):
    total_obtained = 0
    for marks in modules.values():
        total_obtained += marks
    total_possible = len(modules) * 100
    percentage = (total_obtained / total_possible) * 100
    print(f"Total marks obtained = {total_obtained} out of {total_possible}")
    print(f"Percentage = {percentage:.2f}%")
#takes input
def module_marks():
    modules = {}
    for i in range(5):
        module_name = input(f"Enter module {i+1} name: ")
        marks = float(input(f"Enter assignment marks for {module_name}: "))
        modules[module_name] = marks
    return modules
result = module_marks()
print("\nModule Assignment Marks:")
for module, marks in result.items():
    print(module, "→", marks)
grade (result)
