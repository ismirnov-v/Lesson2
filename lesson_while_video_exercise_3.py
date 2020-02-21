#Пукт №3 и №4 из задания в видео про цикл while:

def ask_user():
    while True:
        user_say = input('Как дела? ').strip().lower().capitalize()
        
        if user_say == 'Хорошо':
            return (f'Если у вас все "{user_say}"", то это Замечательно!')
            break

result_ask = ask_user()

print(result_ask)

