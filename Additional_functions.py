"""
Файл с дополнительными функциями для ввода данных и генерации случайных данных.
"""
import random

def is_int(choice):
    """
    Проверка на то, что s - целое число.
    :param choice: Строка для проверки.
    :type choice: str
    :return: True, если строка является целым числом, иначе False.
    :rtype: bool
    """
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

def input_large_number():
    """
    Функция для ввода большого числа и преобразования его в массив цифр.
    :return: Массив цифр, представляющий большое число.
    :rtype: list
    """
    number_str = input("Введите большое число: ")
    number_array = [int(number) for number in number_str]
    return number_array

def generate_random_number(length):
    """
    Функция для генерации случайного большого числа заданной длины.
    :param length: Длина генерируемого числа.
    :type length: int
    :return: Массив цифр, представляющий случайное большое число.
    :rtype: list
    """
    number_array = [random.randint(0, 9) for _ in range(length)]
    return number_array

def input_number_array():
    """
    Функция для ввода массива чисел, разделенных пробелами.
    :return: Массив чисел.
    :rtype: list
    """
    input_str = input("Введите числа, разделенные пробелами: ")
    number_array = [int(number) for number in input_str.split()]
    return number_array

def generate_random_array(length):
    """
    Функция для генерации случайного массива чисел от 1 до 100 заданной длины.
    :param length: Длина генерируемого массива.
    :type length: int
    :return: Случайный массив чисел.
    :rtype: list
    """
    number_array = [random.randint(1, 100) for _ in range(length)]
    return number_array

def input_matrix():
    """
    Функция для ввода матрицы.
    :return: Матрица, введенная пользователем.
    :rtype: list
    """
    m = int(input("Введите количество строк (m): "))
    n = int(input("Введите количество столбцов (n): "))
    matrix = []
    print("Введите элементы матрицы по строкам (разделенные пробелами):\n"
          "В каждой строке должно быть по", n, "элементов")
    for i in range(m):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        if len(row) == n:
            matrix.append(row)
        else:
            print(f"Ошибка: Введено неверное количество элементов в строке {i + 1}. Пожалуйста, введите {n} элементов.")
            return input_matrix()  # Повторить ввод строки
    return matrix

def generate_random_matrix():
    """
    Функция для генерации случайной матрицы.
    :return: Случайная матрица.
    :rtype: list
    """
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
    return matrix

def transpose_list_comprehension(matrix):
    """
    Функция для транспонирования матрицы.
    :param matrix: Исходная матрица.
    :type matrix: list
    :return: Транспонированная матрица.
    :rtype: list
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
