file = open("/Users/sagarmishra841/Desktop/IPPS/Tutorials/Week 7/data.txt", "r")
longest = []  
max_length = 0  
line = file.readline()
while line != "":
    splitline = line.split()
    for i in splitline:
        if len(i) > max_length:
            max_length = len(i)
            longest.clear() 
            longest.append(i)
        elif len(i) == max_length:
            longest.append(i)
    line = file.readline() 
file.close()
print("Longest word(s):",end ="")
for i in longest:
    print (i,end="")
