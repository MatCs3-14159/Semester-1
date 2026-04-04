n = int(input("Enter the size of the grid: "))
print("      ", end="") 
for i in range(1, n+1):
    print(f"{i:02}", end=" ")
print() 
for i in range(1, n+1):
    print(f"{i:02}", end=" ")
    for j in range(1, n+1):
        print(f"{i*j:02}", end=" ")  
    print() 
