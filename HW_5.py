#1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self):
        b_1 = Battery('10 %')
        b_2 = Battery('20 %')
        self.batteries = [b_1.percent_of_battery, b_2.percent_of_battery]


class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, percent_of_battery):
        self.percent_of_battery = percent_of_battery


#2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, song):
        self.song = song
    def play_musik(self):
        print(self.song)


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, mysic):
        self.mysic = mysic
    def music_return(self):
        return self.mysic


my_music = GuitarString('la-la_la')

my_guitar = Guitar(my_music.music_return())
my_guitar.play_musik()



#3
class Calc:
    """
    Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def add_nums(self):
        return self.a + self.b + self.c

c = Calc(1,2,3)

print(c.add_nums())


#4*.

class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)

pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)

#5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitor_num = 50

    def __setattr__(self, key, value):
        if key == 'visitors_count' and value < self.max_visitor_num:
            return object.__setattr__(self, key, value)
        return object.__setattr__(self, key, self.max_visitor_num)



Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 20
print(concert.visitors_count)




#6.
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday
    (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int
fedir = AddressBookDataClass(1234, 'Fedir', '3372832', 'Fedir street, 1', 'fedir@ukr.net', '01.01.1900', 122)
print(fedir.email)


#7. Create the same class (6) but using NamedTuple


from collections import namedtuple

Names = namedtuple('Names', ['key', 'name', 'phone_number', 'address', 'email', 'birthday' , 'age'])
Fedir = Names(1234, 'Fedir', '3372832', 'Fedir street, 1', 'fedir@ukr.net', '01.01.1900', 122)
print(Fedir.key)


#8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='',
    email='', birthday= '', age='')
    """
    def __init__(self, key = '', name='', phone_number='', address='', email='', birthday= '', age = 0):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
    def print_info_adress_book(self):
        print(f"key='{self.key}', name='{self.name}', phone_number='{self.phone_number}', address='{self.address}',"
              f" email='{self.email}', birthday= '{self.birthday}', age='{self.age}'")


fedir_hynnynets = AddressBook(1234, 'Fedir', '3372832', 'Fedir street, 1', 'fedir@ukr.net', '01.01.1900', 122)
fedir_hynnynets.print_info_adress_book()



#9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

Person.age = 100
print(Person.age)


#10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(123, 'Fedir')
setattr(student, 'email', 'fedir@ukr.net' )
print(student.__dict__)
setattr(student, 'student_email', 'stdent_1@ukr.net')
print(getattr(student, 'student_email'))
