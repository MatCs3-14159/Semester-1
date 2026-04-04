line = "H e l l o W o r l d \n"
count = 0
for ch in line:
    if ch not in (" ", "\n"):
        count+=1
print (count)
