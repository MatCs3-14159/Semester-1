numbers = [[1,2,3],[4,5,6],[7,8,9]]
for row in numbers:         
    for value in row:
        print(value, end=" ")

numbers = [[1,2,3], [4,5,6], [7,8,9]]
for row in numbers:         
    for value in row:
        print(value, end=" ")
    print ( )
print(f"\n")

table = []  
for i in range(1, 11):  
    row = []
    for j in range(1, 11):  
        row.append(i * j)
    table.append(row)  
for row in table:
    for value in row:
        print(f"{value:4}", end="")
    print()  

