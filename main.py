"""
Главный файл проекта, содержащий меню для выбора задачи, ввода данных и выполнения алгоритмов.
"""
from Main_functions import *
from Additional_functions import is_int

def display_menu():
    return ("Выберите пункт меню:\n"
            "1. Выбор задачи\n"
            "2. Ввод исходных данных, как вручную, так и сгенерированных случайным образом\n"
            "3. Выполнение алгоритма по заданию\n"
            "4. Вывод результата\n"
            "0. Завершение работы программы")

def display_task_menu():
    return ("Выберите номер задачи:\n"
            "1. Входные данные: 2 массива с цифрами, каждый представляет собой большое число.\n"
            "Нужно произвести сумму или разность массивов.\n"
            "2. Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел.\n"
            "Также, число будет считаться общим, если оно входит в один массив,\n"
            "а в другом массиве находится его перевернутая версия.\n"
            "3. Входные данные: матрица N на M. Требуется повернуть матрицу на 90\n"
            "градусов против часовой или по часовой.")

def menu():
    """
    Основная функция меню, которая позволяет пользователю выбрать задачу, ввести данные и выполнить алгоритмы.
    """
    state = {
        'array1': [],
        'array2': [],
        'matrix': [],
        'choice_task': '',
        'final_result': 0,
        'task_selected': False,
        'data_entered': False,
        'algorithm_executed': False
    }
    choice_handlers = {
        1: handle_task_selection,
        2: handle_data_input,
        3: handle_algorithm_execution,
        4: handle_result_display,
        0: handle_exit
    }
    while True:
        print(display_menu())
        choice = int(input("Введите номер пункта: "))
        handler = choice_handlers.get(choice, handle_error)
        state = handler(state)

def handle_task_selection(state):
    print(display_task_menu())
    choice_task = input("Введите номер задачи: ")
    if is_int(choice_task):
        return {**state, 'choice_task': int(choice_task), 'task_selected': True}
    else:
        print("Ошибка: Введите корректный номер задачи.")
        return state

def handle_data_input(state):
    data_input_handlers = {
        1: input_two_mas,
        2: input_two_numbers_mas,
        3: get_matrix
    }
    if state['task_selected']:
        array1, array2 = data_input_handlers.get(state['choice_task'], lambda x, y: (x, y))(state['array1'], state['array2'])
        return {**state, 'array1': array1, 'array2': array2, 'data_entered': True}
    else:
        print("Сначала выполните пункт 1.")
        return state

def handle_algorithm_execution(state):
    algorithm_handlers = {
        1: sum_or_difference_arrays,
        2: count_total_numbers,
        3: rotation_matrix
    }
    if state['task_selected'] and state['data_entered']:
        final_result = algorithm_handlers.get(state['choice_task'], lambda x, y: 0)(state['array1'], state['array2'])
        return {**state, 'final_result': final_result, 'algorithm_executed': True}
    else:
        print("Сначала выполните пункты 1 и 2.")
        return state

def handle_result_display(state):
    result_display_handlers = {
        1: lambda: print("Итог выполнения алгоритма:", state['final_result']),
        2: lambda: print("Итог выполнения алгоритма:", state['final_result']),
        3: lambda: print("Итог выполнения алгоритма:\n", "\n".join(map(str, state['matrix'])))
    }
    if state['task_selected'] and state['data_entered'] and state['algorithm_executed']:
        result_display_handlers.get(state['choice_task'], lambda: None)()
    else:
        print("Сначала выполните пункты 1, 2, 3.")
    return state

def handle_exit(state):
    exit()

def handle_error(state):
    print('Ошибка: Неверный выбор. Пожалуйста, попробуйте снова.')
    return state

if __name__ == "__main__":
    menu()
