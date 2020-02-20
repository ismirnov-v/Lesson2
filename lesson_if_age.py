user_age = int(input('Введите ваш возраст: '))

# Использовал для отладки
#print(f'Пользователь ввел: {user_age}.')

def user_need_do(user_age):
    """Дает жизненный совет, на вход принимает целое число."""
    user_age = abs(user_age)
    if user_age < 3:
        return 'Вы еще слишком маленький, вам надо быть дома с родителями.'
    elif 3 <= user_age <= 6:
        return 'Вы должны ходить в Детский сад.'
    elif 7 <= user_age <= 18:
        return 'Вы должны учится в школе.'
    elif 19 <= user_age <= 24 or 65 <= user_age <= 99:
        return 'В вашем возрасте нужно учится в ВУЗе'
    elif 25 <= user_age <= 64:
        return 'Вы должны работать.'
    else:
        return 'Может быть вам пора отдохнуть?'

    
user_suggestion = user_need_do(user_age)

print(user_suggestion)