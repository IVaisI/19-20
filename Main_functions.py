"""
Файл с основными функциями для выполнения задач.
"""
from Additional_functions import *

def input_two_mas(array1, array2):
    """
    Функция для ввода двух массивов, представляющих большие числа.
    :param array1: Исходный массив, представляющий первое большое число.
    :type array1: list
    :param array2: Исходный массив, представляющий второе большое число.
    :type array2: list
    :return: Два массива, представляющие большие числа, введенные пользователем или сгенерированные случайным образом.
    :rtype: tuple
    """
    print("Выберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input("Введите номер опции: ")
    option_handlers = {
        1: lambda: (input_large_number(), input_large_number()),
        2: lambda: (generate_random_number(int(input("Введите количество цифр в случайном массиве: "))),
                    generate_random_number(int(input("Введите количество цифр в случайном массиве: "))))
    }
    if is_int(option):
        array1, array2 = option_handlers.get(int(option), lambda: (array1, array2))()
    else:
        print('Ошибка: Введите корректный номер опции.')
        return array1, array2

    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2  # Возвращаем массивы

def sum_or_difference_arrays(array1, array2):
    """
    Функция для вычисления суммы или разности двух массивов.
    :param array1: Первый массив.
    :type array1: list
    :param array2: Второй массив.
    :type array2: list
    :return: Сумма или разность элементов двух массивов.
    :rtype: int
    """
    print("Выберите находить сумму или разность массивов:\n"
          "1. Сумму\n"
          "2. Разность")
    sum_or_difference = input("Введите номер опции: ")
    sum_or_difference_handlers = {
        1: lambda: sum(array1) + sum(array2),
        2: lambda: sum(array1) - sum(array2)
    }
    if is_int(sum_or_difference):
        return sum_or_difference_handlers.get(int(sum_or_difference), lambda: 0)()
    else:
        print('Ошибка: Введите корректный номер опции.')
        return 0

def input_two_numbers_mas(array1, array2):
    """
    Функция для ввода двух массивов чисел.
    :param array1: Исходный массив чисел.
    :type array1: list
    :param array2: Исходный массив чисел.
    :type array2: list
    :return: Два массива чисел, введенные пользователем или сгенерированные случайным образом.
    :rtype: tuple
    """
    print("Выберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input("Введите номер опции: ")
    option_handlers = {
        1: lambda: (input_number_array(), input_number_array()),
        2: lambda: (generate_random_array(int(input("Введите количество цифр в случайном массиве: "))),
                    generate_random_array(int(input("Введите количество цифр в случайном массиве: "))))
    }
    if is_int(option):
        array1, array2 = option_handlers.get(int(option), lambda: (array1, array2))()
    else:
        print('Ошибка: Введите корректный номер опции.')
        return array1, array2

    print("Первый массив:", array1)
    print("Второй массив:", array2)
    return array1, array2  # Возвращаем массивы

def count_total_numbers(array1, array2):
    """
    Функция для подсчета количества общих чисел в двух массивах, включая перевернутые версии.
    :param array1: Первый массив чисел.
    :type array1: list
    :param array2: Второй массив чисел.
    :type array2: list
    :return: Количество общих чисел в двух массивах.
    :rtype: int
    """
    result = sum(1 for i in array1 for j in array2 if i == j or str(i)[::-1] == str(j))
    return result

def get_matrix():
    """
    Функция для ввода матрицы или генерации случайной матрицы.
    :return: Матрица, введенная пользователем или сгенерированная случайным образом.
    :rtype: list
    """
    print("Выберите опцию 1-2:\n"
          "1. Ввести матрицу самостоятельно\n"
          "2. Сгенерировать матрицу случайным образом\n")
    option = input("Введите номер опции: ")
    option_handlers = {
        1: input_matrix,
        2: generate_random_matrix
    }
    if is_int(option):
        matrix = option_handlers.get(int(option), lambda: [])()
    else:
        print("Ошибка: Введите корректный номер опции.")
        return []

    print("Начальная матрица:\n")
    for row in matrix:
        print(row)
    return matrix

def rotation_matrix(matrix):
    """
    Функция для поворота матрицы на 90 градусов против часовой стрелки.
    :param matrix: Исходная матрица.
    :type matrix: list
    :return: Повернутая матрица.
    :rtype: list
    """
    transposed_matrix = transpose_list_comprehension(matrix)
    rotated_matrix = [row for row in transposed_matrix[::-1]]
    return rotated_matrix
