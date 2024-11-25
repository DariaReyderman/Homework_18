# Exersice 1

tup_a: tuple[int] = (99,)
print('a', tup_a)

tup_b: tuple[int, int, int] = (77, 88, 99)
print('b', tup_b)


def tuple_c(c: tuple) -> int:
    return len(c)


print('c', tuple_c((1, 2, 3, 4, 5)))


def tuple_d(x: tuple, y: tuple) -> tuple:
    return x + y


print('d', tuple_d((6,7), (8, 9)))


def tuple_e(x: tuple, y: tuple) -> tuple:
    same_numbers = []
    for number in x:
        if number in y and number not in same_numbers:
            same_numbers.append(number)
    return tuple(same_numbers)


x = (1, 2, 3, 4)
y = (3, 4, 5, 6)
print('e', tuple_e(x, y))


def tuple_f(x: tuple, y: tuple) -> tuple:
    different_numbers = []
    for number in x:
        if number not in y and number not in different_numbers:
            different_numbers.append(number)
    for number in y:
        if number not in x and number not in different_numbers:
            different_numbers.append(number)
    return tuple(different_numbers)


x1 = (1, 2, 3, 4)
y1 = (3, 4, 5, 6)
print('f', tuple_f(x, y))


def tuple_g(tup, index) -> int | None:
    if 0 <= index < len(tup):
        return tup[index]
    else:
        return None


print('g', tuple_g((23, 4, 89, 0), 2))


def tuple_h(h: tuple) -> tuple:
    tup_reverse: list[any] = []
    for item in h:
        if item not in tup_reverse:
            tup_reverse.append(item)
    return tuple(tup_reverse[::-1])


print('h', tuple_h(('hello', 'Python', 'Dear')))


def tuple_i(tup: tuple, num: int) -> tuple:
    return tup * num


print('i', tuple_i((7, 8, 9), 3))


def tuple_j(tup: tuple, num: int) -> tuple:
    return tuple(number for number in tup if number != num)


print('j', tuple_j((10, 8, 5, 5, 3, 2, 50, 10, 30, 40), 10))


def tuple_k(k: tuple[any]) -> tuple:
    list1 = []
    for item in k:
        if item not in list1:
            list1.append(item)
    return tuple(list1)


print('k', tuple_k((1, 2, 2, 3, 4, 5, 3)))


def tuple_l(l: tuple, n: int) -> tuple:
    list2: list[int] = []
    index: int = 0
    for item in l:
        if item == n:
            list2.append(index)
        index += 1
    return tuple(list2)


print('bonus l', tuple_l((10, 8, 5, 5, 3, 2, 5, 10, 30, 40), 5))

names: list[str] = []
grades: list[int] = []
while True:
    name: str = input("Enter your name: ")
    if name == "done":
        break
    names.append(name)
while True:
    grade: int = int(input("Enter your grade: "))
    if grade == -999:
        break
    grades.append(grade)
names_grades: tuple[tuple[any]] = tuple(zip(names, grades))
print('m', names_grades)

# Exercise 2
# Tuple is an ordered collection of elements that cannot be modified, unlike lists. Tuples are best used to store
# persistent data, and lists are best used to store data that may require editing in the future.

# Exercise 3
# The code
data_tuple = ({"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code")
data_tuple[0]["age"] = 31
data_tuple[0].clear()
# doesn't throw an error because if there is a mutable objects (dictionary, list) inside the tuple - we can change
# them. We can't change the tuple itself.
