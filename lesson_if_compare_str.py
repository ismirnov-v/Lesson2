# Практика: Сравнение строк.


def check_and_compare_input(first_str, second_str):
    """Функция для сравнения двух строк которые будут введены пользователем."""
    first_str = input('Это строка №1, введите текст: ')
    second_str = input('Это строка №2, введите текст: ')
    if type(first_str) != str or type(second_str) != str:
        return 0
    elif first_str == second_str:
        return 1
    elif first_str != second_str and len(first_str) > len(second_str):
        return 2
    elif first_str != second_str and second_str == 'learn':
        return 3
    

def call_func(check_and_compare_input):
    """Метод вызова функции для печати результата ее работы, на вход ожидает имя функции которая принимает два параметра."""
    result = check_and_compare_input(first_str='', second_str='')
    print(f'Функция вернула: {result}')


call_func(check_and_compare_input)
call_func(check_and_compare_input)
call_func(check_and_compare_input)
