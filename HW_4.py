"""1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed,
mileage_info"""


class Vehicle:
    def __init__(self, max_speed=100, mileage=10000):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print('increase_speed')

    def break_speed(self):
        print('break_speed')

    def mileage_info(self):
        print(f'mileage {self.mileage} miles.')


'''2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме 
власний метод seating_capacity'''


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super(Bus, self).__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def seating_capacity(self):
        print(f'seating_capacity is {self.seating_capacity} persons')


'''3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)'''
print(issubclass(Bus, Vehicle))

'''4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus'''

school_bus = Bus(100, 20000, 50)
print(isinstance(school_bus, Bus))
print(isinstance(school_bus, Vehicle))

'''5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами 
school_address, main_subject'''


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print('c. Colorado, Python street, 1000')

    def main_subject(self):
        print('main_subject is Python')


'''6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color'''


class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, seating_capacity, get_school_id, number_of_students, bus_school_color):
        super().__init__(get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def return_information(self):
        print(
            f'max_speed {self.max_speed}, mileage {self.mileage}, capacity {self.seating_capacity}, '
            f'get_school_id {self.get_school_id}, number_of_students {self.number_of_students},'
            f' bus_school_color {self.bus_school_color}'
        )


school_bus_1 = SchoolBus('100 m/h', '20000 m', 100, '1.1.1.1', 10, 'Green')
school_bus_1.return_information()

'''# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри:
 від Ведмідь і від Вовк, створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.'''


class Bear:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def eat(self):
        print('Bear eats')


class Wolf:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def eat(self):
        print('Wolf eats')


vovchyk_bratyk = Wolf('Vovchyk_bratyk', '100 kg')
balu = Bear('Balu', '100 kg')

for forest_animal in vovchyk_bratyk, balu:
    forest_animal.eat()

'''Магічні методи:
Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише
коли population > 1500, інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього 
завдання магічні методи'''


class City:
    def __new__(cls, *args, **kwargs):
        n, p = args
        if p > 1500:
            print(f'The city {n} with a population {p} is created')
            return super().__new__(cls)
        else:
            print(f'Your city {n} is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population


kyiv = City('Kyiv', 2000)
selo = City('Selo', 1000)
