from models.models import Employee, Salon, Plant
import pprint


class Controler:
    @staticmethod
    def print_menu():
        pprint.pprint(
            [
                "1. Add new plant",
                "2. Get all plants",
                "3. Get plant by id",
                "4. Delete plant by id",
                "5. Add new employee with salon or without",
                "6. Get all employee",
                "7. Get employee by id",
                "8. Delete employee by id",
                "9. Add salon by name",
                "10. Delete salon by id",
            ]
        )

    @staticmethod
    def Add_new_plant(name, location):
        plant = Plant(name, location)
        plant.save()

    @staticmethod
    def Get_all_plants():
        plants = Plant.get_all()
        pprint.pprint(*(plant for plant in plants))

    @staticmethod
    def Get_plant_by_id(id):
        plant = Plant.get_by_id(id)
        print(plant)

    @staticmethod
    def Delete_plant_by_id(id):
        Plant.delete(id)

    @staticmethod
    def Add_new_employee_with_salon_or_without(name, email, plant_id, salon=None):
        if salon:
            employee = Employee(name, email, plant_id, salon)
            employee.save()
            s = Salon(salon)
            s.save()
        else:
            employee = Employee(name, email, plant_id)
            employee.save()

    @staticmethod
    def Get_all_employee():
        employees = Employee.get_all()
        pprint.pprint(*(e for e in employees))

    @staticmethod
    def Get_employee_by_id(id):
        employee = Employee.get_by_id(id)
        print(employee)

    @staticmethod
    def Delete_employee_by_id(id):
        Employee.delete(id)

    @staticmethod
    def Add_salon_by_name(name):
        salon = Salon(name)
        salon.save()

    @staticmethod
    def Delete_salon_by_id(id):
        Salon.delete(id)
