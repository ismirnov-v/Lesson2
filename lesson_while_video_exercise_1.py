# Пункт №1 по заданию из видео про цикл while.

list_names = ['Вася', 'Маша','Петя', 'Валера', 'Валера', 'Саша', 'Даша']

while True:
    name = (list_names.pop())
    
    if name == 'Валера':
        print('Валера нашелся!')
        break