import logging

from HW_10.app.framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id

    def save(self):
        plant = Plant.get_by_id(self.plant_id)
        try:
            self.employee_validator()
        except ValueError:
            logging.error("Not valid data")
            return
        if not plant:
            raise ValueError("Plant not found!")
        super().save()

    def employee_validator(self):  # додали мінімальний валідатор employee
        if len(self.name.split()) != 2:
            print("name must have two or more words")
            raise ValueError("Not valid name")
        data = self.get_all()
        for el in data:
            if self.email == el["email"]:
                raise ValueError("This email already exist!")
        if not "@" in self.email or not "." in self.email:
            raise ValueError("Not a valid email address!")
        position = self.email.find("@")
        position_of_dot = self.email.find(".")
        if position > position_of_dot:
            raise ValueError("Not a valid email address!")
