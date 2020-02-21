#Переписываем функцию, чтобы она могла обработат исключения - не корректный ввод параметров.


def discounted(price, discount, max_discounted=20):
    try:
        #price = abs(float(price))
        discount = abs(float(discount))
        max_discounted = abs(float(max_discounted))

        if max_discounted > 99:
            raise ValueError('Слишком большая максимальная скидка.')
        if discount >= max_discounted:
            return price
        else:
            return price * (1 - discount/100)
    except TypeError:
        print('Функция ожидает на вход, числа.')


#Проверяем:

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': '65432.1', 'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}
phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}

apple_desc = discounted(phone1['price'], phone1['discount'])

android_desc = discounted(phone2['price'], phone2['discount'])
print(android_desc)

noname_desc = discounted(phone3['price'], phone3['discount'])
print(noname_desc)

