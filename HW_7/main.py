from models.models import Plant, Employee

while True:
    print("1. Add new plant \n"
          "2. Get all plants\n"
          "3. Get plant by id\n"
          "4. Delete plant by id\n"
          "5. Add new employee\n"
          "6. Get all employee\n"
          "7. Get employee by id\n"
          "8. Delete employee by id\n"
          )
    flag = int(input("Choose: "))
    if flag == 1:
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        plants = Plant.get_all()
        for plant in plants:
            print(plant["id"])
            print(plant["name"])
            print(plant["location"])
    elif flag == 3:
        id = int(input('Type id of plant: '))
        plant = Plant.get_by_id(id)
        print(plant["id"])
        print(plant["name"])
        print(plant["location"])
    elif flag == 4:
        id = int(input('Type id of plant which you want to delete: '))
        Plant.delete(id)
    elif flag == 5:
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        plant_id = int(input("Type id of plant: "))
        employee = Employee(name, email, plant_id)
        employee.save()
    elif flag == 6:
        employees = Employee.get_all()
        for employee in employees:
            print(employee["id"])
            print(employee["name"])
            print(employee["email"])
    elif flag == 7:
        id = int(input('Type id of employee: '))
        employee = Employee.get_by_id(id)
        print(employee["id"])
        print(employee["name"])
        print(employee["email"])
    elif flag == 8:
        id = int(input('Type id of employee: '))
        Employee.delete(id)





# file = open("test.txt", "a")
# file.write("a")
# file.close()