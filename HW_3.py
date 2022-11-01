# 1. Define the id of next variables:
int_a = 55
print(id(int_a))
str_b = "cursor"
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {"a": 1, "b": 2, "c": 3}
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# 3. Define the type of each object from step 1.
print(list(map(type, (int_a, str_b, set_c, lst_d, set_c, dict_e))))

# 4. Check the type of the objects by using isinstance
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

'''String formatting:
Replace the placeholders with a value:
"Anna has ___ apples and ___ peaches."'''

apples = 5
peaches = 10

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(apples, peaches))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(peaches, apples))

# 7. By using keyword arguments into the curly braces.
print("Anna has {a} apples and {p} peaches.".format(p=peaches, a=apples))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:>5d} apples and {1:>3d} peaches.".format(apples, peaches))

# 9. With f-strings and variables
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator
print("Anna has %s apples and %s peaches." % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
d = {apples: 5, peaches: 10}
print(f"Anna has {d[apples]} apples and {d[peaches]} peaches.")

# 12. Convert (1) to list comprehension
"""(1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)"""

lst = [num**2 if num % 2 == 1 else num**4 for num in range(10)]
print(lst)

# 13. Convert (2) to regular for with if-else
"""(2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]"""

list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)

print(list_comprehension)

# 14. Convert (3) to dict comprehension.
"""(3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d) """

d = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(d)

# 15*. Convert (4) to dict comprehension.
"""(4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)"""

d = {num: num**2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}

# 16. Convert (5) to regular for with if.
"""(5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}"""

dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x**3
print(dict_comprehension)

# 17*. Convert (6) to regular for with if-else.
"""(6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}"""

dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x**3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)

# 18. Convert (7) to lambda function
"""(7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y"""

foo = lambda x, y: x if x < y else y

print(foo(3, 5))

# 19*. Convert (8) to regular function
"""(8)
foo = lambda x, y, z: z if y < x and x > z else y"""


def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(3, 8, 4))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

m = list(map(lambda x: x * 2, lst_to_sort))
print(m)


# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

a = [x**y for x, y in zip(list_A, list_B)]
print(a)

b = [*map(lambda i, k: i**k, list_A, list_B)]
print(b)


# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

f = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(f)

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.


def negative(x):
    if x < 0:
        return x


f_1 = tuple(filter(negative, range(-10, 10)))
print(f_1)


# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

a = list(filter(lambda a: a in list_2, list_1))
print(a)
