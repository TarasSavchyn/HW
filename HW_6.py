"""1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
Iterator get numbers of first Fibonacci numbers
Example:

for i in FibonacciNumbers(10):
    print(i)
0
1
1
2
3
5
8
13
21
34
55"""


class FibonacciNumbers:
    a, b, count = 0, 1, 0

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):  # логіка утворення наступного значення послідовності
        if self.count == 0:
            self.count += 1
            return 0
        if self.count < self.n:
            self.count += 1
            self.a, self.b = self.b, self.b + self.a
            return self.a
        else:
            raise StopIteration


for i in FibonacciNumbers(10):
    print(i)


"""2.* Implement generator for Fibonacci numbers"""


def fibonaci(n):  # функція генератор чисел Фібоначі
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(
    [*fibonaci(10)]
)  # друк згенерованих чисел Фібоначі у вигляді списку заданої довжини


"""3. Write generator expression that returns square numbers of integers from 0 to 10"""

generator_expression = (i**2 for i in range(11))

print(generator_expression)  # вивів генератор
print(*generator_expression)  # вивів значення

"""4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface."""

from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def Screen(self):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError

    @abstractmethod
    def Ports(self):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def Screen(self):
        print("Screen")

    def Keyboard(self):
        print("Keyboard")

    def Touchpad(self):
        print("Touchpad")

    def WebCam(self):
        print("WebCam")

    def Ports(self):
        print("Ports")

    def Dynamics(self):
        print("Dynamics")


HP_1 = (
    HPLaptop()
)  # we cannot create an instance without overriding all the necessary methods
# L = Laptop() we cannot instantiate an abstract class

# note = Laptop() TypeError: Can't instantiate abstract class HPLaptop with abstract methods Dynamics, Keyboard, Ports, Screen, Touchpad, WebCam

"""5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
should be abstract."""

# from abc import ABC, abstractmethod


class Car(ABC):
    def drive(self):
        print("car drive")

    def stop(self):
        print("car stop")

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError


class Sedan(Car):
    def open_door(self):
        print("open_door")

    def close_door(self):
        print("close_door")

    def turn_on_light(self):
        print("turn_on_light")

    def turn_off_light(self):
        print("turn_off_light")

    def enable_radio(self):
        print("enable_radio")

    def disable_radio(self):
        print("disable_radio")


ford = (
    Sedan()
)  # перевірили чи можна створити екземпляр по шаблону без методів "drive and stop"
ford.turn_off_light()  # перевірили чи викликаються методи підкласу
ford.stop()  # перевірили чи викликаються методи базового класу
