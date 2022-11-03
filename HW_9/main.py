with open('file.txt', 'w') as i:
    i.write('Hello teacher!!!!\nall done!!!')

"""
TASK 1
Створити логер який дозволяє працювати з файлами як звичайний open,
але разом з тим в файл logs.txt записує:
коли був відкритий файл, назва файла, коли закритий файл
для інформації про час можемо використати datetime.now()
приклад відпрацювання
with my_custom_manager('file.txt', 'r') as f:
    f.read()
В файл буде записано
2022-07-11 22:17:59.782551 file.txt OPEN
2022-07-11 22:18:00.782551 file.txt CLOSE"""

from datetime import datetime as time
from os import listdir




class Log:
    def __init__(self, fn, mode="r"):
        self.fn = open(fn, mode)
        self.mode = mode

    def __enter__(self):

        if self.fn.name in listdir():
            with open("logs.txt", "a") as f:
                f.write(f"{time.now()} {self.fn.name} OPEN\n")
        else:
            with open("logs.txt", "w") as f:
                f.write(f"{time.now()} {self.fn.name} OPEN\n")

        return self.fn

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("logs.txt", "a") as f:
            f.write(f"{time.now()} {self.fn.name} CLOSE\n")
            self.fn.close()


with Log("file.txt", "r") as file:
    print(file.read())


"""TASK 2
Написати ф-цію яка переводить файл logs.txt в logs.csv
Приклад такого файлу
2022-07-11 22:17:59.782551, file.txt, OPEN
2022-07-11 22:18:00.782551, file.txt, CLOSE"""


def reformat_txt_to_csv(file):
    name, typ = file.split(".")

    with open(file, "r") as f:
        context = f.read()

    with open(f"{name}.csv", "w") as f2:
        f2.write(context)


reformat_txt_to_csv("logs.txt")


"""TASK 3 (з зірочкою)
Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
Цю інформацію записати в logs.json. Приклад:
{
    "file.txt": {
        "count": 2,
        "last_time_opened": "2022-07-11 22:17:59.782551"
    }
}"""
import json

log_file_name = "logs.txt"


def log_info_json_saver(log_file_name): # тут без бутилки не розбереш
    with open(log_file_name, "r") as file:
        logs = file.readlines()
    with open(f'{log_file_name.split(".")[0]}.json', "w") as file_2:
        if logs:
            key = logs[0].split()[-2]
            value = {"count": int(len(logs) / 2), "last_time_opened": f"{logs[-2].split()[0]} {logs[-2].split()[1]}"}

        file_2.write(json.dumps({key:value}, indent=4))


log_info_json_saver(log_file_name)
