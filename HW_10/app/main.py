import logging
from models.models import Plant, Employee
from HW_10.app.directory_config import directory_config

date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"

logging.basicConfig(
    filename="logs/main.log",
    format=message_format,
    datefmt=date_strftime_format,
    encoding="UTF-8",
    level=logging.DEBUG,
)


if __name__ == "__main__":  # проводимо налаштування папки для роботи
    directory_config()


while True:
    print(
        "1. Add new plant \n"
        "2. Get all plants\n"
        "3. Get plant by id\n"
        "4. Delete plant by id\n"
        "5. Add new employee\n"
        "6. Get all employee\n"
        "7. Get employee by id\n"
        "8. Delete employee by id\n"
    )
    logging.info("Menu printed!!!")

    try:
        flag = int(input("Choose: "))
        if flag not in range(1, 9):
            raise ValueError

    except ValueError as e:
        logging.error(e)
        print("You must to type a number in range 1-8 !!!")
        continue

    if flag == 1:
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()
        logging.info(f'new plant "{name}" is added')
    elif flag == 2:
        plants = Plant.get_all()
        for plant in plants:
            print(plant["id"])
            print(plant["name"])
            print(plant["location"])
    elif flag == 3:
        try:
            id = int(input("Type id of plant: "))
        except ValueError as e:
            print('"id" must be a number')
            logging.error(e)
            continue
        try:
            plant = Plant.get_by_id(id)
            print(plant["id"])
            print(plant["name"])
            print(plant["location"])
        except TypeError:
            print("Non-existent id entered")
            logging.error("Non-existent id entered")

    elif flag == 4:
        try:
            id = int(input("Type id of plant which you want to delete: "))
        except (ValueError, TypeError):
            logging.error("Non-existent id entered")

        try:
            Plant.delete(id)
            logging.info(f"the Plant with id: {id} has been removed")
        except ValueError:
            logging.error("Non-existent id entered")

    elif flag == 5:
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        try:
            plant_id = int(input("Type id of plant: "))
        except ValueError:
            logging.error("plant_id must be a number")

        try:
            employee = Employee(name, email, plant_id)
        except NameError:
            print("data entry error")
        try:
            employee.save()
            logging.info(f"new employee {name} is added")
        except ValueError as e:
            logging.error(e)
            print("You need to write a plant_id of existing plant!")

    elif flag == 6:
        employees = Employee.get_all()
        for employee in employees:
            print(employee["id"])
            print(employee["name"])
            print(employee["email"])
    elif flag == 7:
        try:
            id = int(input("Type id of employee: "))
        except (ValueError, TypeError):
            print('"id" must be a number')
            logging.error("Id of employee not a number")
            continue
        employee = Employee.get_by_id(id)
        try:
            print(employee["id"])
            print(employee["name"])
            print(employee["email"])
        except TypeError:
            print("Non-existent id entered")
    elif flag == 8:
        try:
            id = int(input("Type id of employee: "))
        except ValueError:
            logging.error("Id of employee not a number")

        try:
            Employee.delete(id)
            logging.info(f"the employee with id: {id} has been removed")
        except ValueError:
            logging.error("Non-existent id entered")
