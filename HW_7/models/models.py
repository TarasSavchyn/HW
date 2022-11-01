from HW_7.framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name: str, email: str, plant_id: int, salon=None):
        self.name = name
        self.email = email
        self.plant_id = plant_id
        if salon:
            self.salon = salon


class Salon(Model):
    file = "salon.json"

    def __init__(self, name: str):
        self.name = name
