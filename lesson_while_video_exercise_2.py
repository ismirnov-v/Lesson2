#Пункт №2 задания из видео про цикл while:
#Пишем функцию для поиска строки в списке.

list_names = ['Вася', 'Маша','Петя', 'Валера', 'Валера', 'Саша', 'Даша']

def find_person(list_names, user_name):
    """ Функция принимает на вход список и строку, и выполняет поиск строки в списке"""
    while True:
        name = (list_names.pop())
        
        if user_name  == name:
            return (f'Пользователь "{user_name}" найден!')
            break

#Проверка функции:
search_result = find_person(list_names, 'Маша')
print(search_result)