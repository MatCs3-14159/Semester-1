#first way

list_num = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(list_num)):
    if i %2 == 0:
        a = list_num[i]**2
        del list_num[i]
        list_num.insert(i, a)
print (list_num)

#Second way

list_num = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(list_num)):
    if i %2 == 0:
        list_num[i] = list_num[i]**2
print (list_num)
