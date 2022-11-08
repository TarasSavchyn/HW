import logging
from os import stat, mkdir, listdir


def directory_config():
    if "database" not in listdir():
        mkdir("database")
        logging.warning('created directory "database"')

    if (
        "plants.json" not in listdir("database")
        or stat("database/plants.json").st_size == 0
    ):
        with open("database/plants.json", "w") as p:
            p.write("[]")
        logging.warning('created file "plants.json')

    if (
        "employees.json" not in listdir("database")
        or stat("database/employees.json").st_size == 0
    ):
        with open("database/employees.json", "w") as e:
            e.write("[]")
        logging.warning('created file "employees.json"')
