import logging
from os import stat, mkdir, listdir
import json


def directory_config():

    if "database" not in listdir():
        mkdir("database")
        logging.warning('created directory "database"')

    if (
        "plants.json" not in listdir("database")
        or stat("database/plants.json").st_size == 0
    ):
        with open("database/plants.json", "w") as p:
            p.write(json.dumps([]))
        logging.warning('created file "plants.json')

    if (
        "employees.json" not in listdir("database")
        or stat("database/employees.json").st_size == 0
    ):
        with open("database/employees.json", "w") as e:
            e.write(json.dumps([]))
        logging.warning('created file "employees.json"')

    with open("database/plants.json", "r") as p:
        try:
            data = json.load(p)
        except:
            logging.error("json  error file plants.json")
            with open("database/plants.json", "w") as p:
                p.write(json.dumps([]))
            logging.warning("created new file plants.json ")

        try:
            if sorted(["name", "location", "id"]) != sorted([d for d in data[0]]):
                with open("database/plants.json", "w") as p:
                    p.write(json.dumps([]))

        except:
            pass

    with open("database/employees.json", "r") as e:
        try:
            data = json.load(e)
        except:
            logging.error("json error file employee.json")
            with open("database/employees.json", "w") as e:
                e.write(json.dumps([]))
            logging.warning("created new file employees.json ")

        try:
            if sorted(["name", "email", "plant_id", "id"]) != sorted(
                [d for d in data[0]]
            ):
                with open("database/employees.json", "w") as e:
                    e.write(json.dumps([]))
        except:
            pass
