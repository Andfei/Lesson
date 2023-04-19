'''
написать функцию, которая находит максимальное значение в списке (без использования функции max) и с использованием цикла while
'''
list_ = [
    [[12, 14, 10], [56, 78, 90]],
    [[56, 32, 1, 10], [-1, 2, 67, 90]],
    [[100, 102, 56], [78, 65, 43]]
]

def func(matrix):
    matrix = sum(matrix, [])
    matrix = sum(matrix, [])
    elem = 0
    max_elem = 0
    while elem < len(matrix):
        if max_elem <= matrix[elem]:
            max_elem = matrix[elem]
        elem += 1
    return max_elem


print(func(list_))
'''
написать программу для вычисления факториала. Факториал - 1 * 2 * 3 ... * n
'''
namber = int(input("Input namder:"))


def factorial(namber):
    sum = 1
    for i in range(namber):
        sum = sum*(i+1)
    return sum


print(factorial(namber))
'''
Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Нужно вернуть список, который состоит из элементов, общих для этих двух списков
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def add_new_list(a , b):
    res = a + b
    res = list(set(res))
    return res


print(add_new_list(a, b))
'''
Написать декоратор, который будет просить пользователя ввести число до тех пор, пока он не введет положительное число
'''
namber = -1


def decorator_result(function_to_decorate):
    def wrapper(arg):
        while arg < 0:
            arg = int(input("Input namber:"))
            if arg > 0:
                function_to_decorate(arg)
    return wrapper


@decorator_result
def func(number):
    print(number)
    return number


func(namber)
'''
Написать декоратор, который проверяет, есть ли у пользователя birth_year, если есть, то мы его удаляем и записываем age
'''
def decorator_result(function_to_decorate):
    def wrapper(arg):
        if "birth_year" in arg:
            arg["age"] = 2023 - arg["birth_year"]
            arg.pop('birth_year')
        function_to_decorate(arg)
    return wrapper


@decorator_result
def func(person):
    print(person) # хотим увидеть {"name": "Petr", "age": 31}
    return person

func({"name": "Petr", "birth_year": 1992})
'''
Выполняется только 3 раза после 3 раза выводит ошибку
'''
count = 0
def counter(func):
    def inner_wrapper(*args, **kwargs):
        global count
        count += 1
        if count <= 3:
            func(*args, **kwargs)
            print(f"Count: {count}")
        else:
            print("Warning!!!")
    return inner_wrapper


@counter
def say():
    print("meow")


say()
say()
say()
say()
say()
say()
say()