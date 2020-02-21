#Пукт №4 из задания в видео про цикл while (совпадает с пунктами 2  и 3 в задании из слайдов):

questioin_dictionary = {
    'Как дела?': 'Нормуль.',
    'Как поживаешь?': 'Все в порядке.',
    'Пойдеш гулять?': 'Да, завтра после 14:00.',
    'Чем занимаешся?': 'Мучаю WSL.',
    'Что тебе нравится?': 'Отвечать на вопросы.',
    'У тебя есть хобби?': 'Да',
}

questioin_stop = {
    'Хватит вопросов': 'Как скажешь!',
}


def ask_user():
    """Отвечает на вопросы пользоателя, ответы берет из словаря.
    Выходит из цикла, если пользователь напишет "Хватит вопросов"
    """
    while True:
        user_say = input('Напиши что хочешь спросить: ').strip().lower().capitalize()
        if user_say in questioin_stop:
            return (f'{questioin_stop.get(user_say, 0)}')
        if user_say in questioin_dictionary:
            print(f'{questioin_dictionary.get(user_say, 0)}')
        else:
            print('Я не знаю ответа на данный вопрос.')
            print('---------------')
            continue
         

result_ask = ask_user()

print(result_ask)