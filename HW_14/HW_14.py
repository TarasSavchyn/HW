"""# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    pass

def add(a, b):
    return a + b

add(5, 5)  # 10

@double_result
def add(a, b):
    return a + b

add(5, 5)  # 20"""


def double_result(funk):
    def wrapper(*args):
        res = funk(*args)
        print(f"double_result {res * 2}")
        return res

    return wrapper


@double_result
def add(a, b):
    return a + b


print(add(2, 5))


"""# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    pass


@only_odd_parameters
def add(a, b):
    return a + b


add(5, 5)  # 10
add(4, 4)  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e"""


def only_odd_parameters(funk):
    def wrapper(*args):
        for i in args:
            if i % 2 == 0:
                return "Please use only odd numbers!"
        return funk(*args)

    return wrapper


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))
print(add(5, 4))


"""# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    # log function arguments and its return value
    pass


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)


# you called func(4, 4, 4)
# it returned 6"""

import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open("HW_14/logs.txt", "a") as file:
            file.write(
                f"{datetime.datetime.now()} args {args}, kwargs {kwargs} res = {func(*args, **kwargs )}\n"
            )
        return res

    return wrapper


@logger
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


print(func(4, 4, 3))
print(func(a=2, b=4, d=3))

"""# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    pass


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function"""


def type_check(parametr_type):
    def argumenter(funk):
        def wrapper(*args, **kwargs):
            if type(args[0]) == parametr_type:
                res = funk(*args, **kwargs)
                return res
            return f"Wrong Type: {type(args[0])} should be printed, since non-{parametr_type} passed to decorated function"

        return wrapper

    return argumenter


@type_check(int)
def times2(num):
    return num * 2


print(times2("ss"))
print(times2(10))
