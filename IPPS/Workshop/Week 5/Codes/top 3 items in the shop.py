name = "Sagar Mishra"
print(name)
#program
shop_items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
def get_value(item):
    return item[1]
sorted_items = sorted(shop_items.items(), key=get_value, reverse=True)
for i in range(3):
    print(f"{sorted_items[i][0]}: {sorted_items[i][1]}")
