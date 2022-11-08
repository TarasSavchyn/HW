import logging

from HW_10.app.framework.models import Model


class Plant(Model): #ДОДАТИ ПЕРЕВІРКИ ПРИ ЛОГУВАННІ
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model): #ДОДАТИ ПЕРЕВІРКИ ПРИ ЛОГУВАННІ
    file = "employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name  # імя повинно бути тільки латинськими буквами "Taras Savchyn"
        self.email = email
        self.plant_id = plant_id  # повинен бути валідний ід наступний номер і тип int()

    def check_email(self):
        data = self.get_all()
        for el in data:
            if self.email == el["email"]:
                raise ValueError("This email already exist!")

    def check_email_format(self):
        if not "@" in self.email or not "." in self.email:
            raise ValueError("Not a valid email address!")
        position = self.email.find("@")
        position_of_dot = self.email.find(".")
        if position > position_of_dot:
            raise ValueError("Not a valid email address!")




    def save(self):
        plant = Plant.get_by_id(self.plant_id)
        try:
            self.check_email()
            self.check_email_format()
        except ValueError as e:
            logging.error(str(e) + " Email: " + self.email)
            print(e)
            return
        if not plant:
            raise ValueError("Plant not found!")
        super().save()
