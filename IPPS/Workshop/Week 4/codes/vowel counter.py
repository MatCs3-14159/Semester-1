user = input ("Enter any word: ")
count = 0
for i in user:
    if i in "aeiouAEIOU":
        count+=1
print ("Number of vowels:",count)
