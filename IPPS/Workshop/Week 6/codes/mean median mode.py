print ("Sagar Mishra")
#program
def improved_average(a):
    #mean
    sum = 0 
    for num in a:
        sum += num
    print(f"Mean = {sum/5:.2f}") 
    #median
    a.sort()
    print("Median = ",a[2])
    #mode
    count_dict = {}
    for num in a:
        found = False
        for key in count_dict:
            if key == num:
                count_dict[key] += 1
                found = True
                break
        if not found:
            count_dict[num] = 1
    max_count = 0
    for key in count_dict:
        if count_dict[key] > max_count:
            max_count = count_dict[key]
    if max_count == 1:
        print("No mode")
    else:
        for key in count_dict:
            if count_dict[key] == max_count:
                print(f"mode = {key} (count {count_dict[key]})")
    print("Numbers count = ",count_dict)
#take inputs 
numbers = []
for i in range(5):
    x = int(input(f"Enter the {i+1}th index number: "))
    numbers.append(x)
#call functions
improved_average(numbers)
