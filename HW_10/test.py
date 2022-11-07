from os import stat

a = stat("app/database/plants.json")
print(a.st_size)
