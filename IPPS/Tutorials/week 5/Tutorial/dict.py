car_owner_information = {"Ram":"Hyundai","Hari":"Hummer","Shyam":"Honda","Ravi":"Honda"}
for car_owner in car_owner_information.values():
    if car_owner == "Honda":
        print (car_owner)

car_owner_information = {"Ram":"Hyundai","Hari":"Hummer","Shyam":"Honda","Ravi":"Honda"}
for car_owner,car in car_owner_information.items():
    if car == "Honda":
        print(car_owner)
