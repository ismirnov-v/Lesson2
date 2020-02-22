from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sec
import logging
import ephem
from datetime import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, 
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def check_constellation(bot, update):
    """Фнукция которая возвращает созведие в котором находится планета, на вход принимает два параметра экземпляр бота и сообщение которое в него пришло."""
    
    def planet_info(user_planet):
        """ Функция возвращает созвездие где находится планета в текущий момент времени.
        На вход ожидает имя планеты"""
        try:
            # C помощью встроенной функции getattr получаем значение атрибута  объекта user_planet.
            planet = getattr(ephem, user_planet)()
            planet.compute(datetime.now())
            return f'В данный момент {user_planet} находится в созвездии:\n {ephem.constellation(planet)}'      
        except AttributeError:
            return f'Я ничего не знаю о {user_planet}'

    # Сеохраняем в переменную планету о которой хочет узнать пользователь.
    user_request = update.message.text.split(" ")
    user_planet = user_request[1].capitalize()

    logging.info(f'На вход пришло: {user_request}. После преобразования получили: "{user_planet}"')
    
    response_result = planet_info(user_planet)
    update.message.reply_text(response_result)
        
def talk_to_me(bot, update):
    """ Простая функция для эхо ответа и записи информации в лог."""
    #Эхоответ:
    user_response = (f'Привет {update.message.chat.first_name}! Ты написал "{update.message.text}".')
    #Логирование:
    logging.info('User: %s, Chat id: %s, Message: %s',
                update.message.chat.username,
                update.message.chat.id,
                update.message.text)
    update.message.reply_text(user_response)

def main():
    """Основная функиця, запускающая бота."""
    #Подключаемся к платформе telegram
    mybot = Updater(sec.key, request_kwargs=sec.PROXY)
    #Пишем информацию в лог.
    logging.info('Бот запускается.')

    #Диспетчер, объект для коммутации входяшего сообшения к подписчику.
    dp = mybot.dispatcher

    #Отслеживаем команды и пердаем их подписчику (вызов функции):
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", check_constellation))

    #Отслеживаем сообщения, и делаем эхос помошью функции talk_to_me.
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    #Начинаем общение с платформой телеграм, для проверки наличия сообщений:
    mybot.start_polling()
    
    #Работать бесконечно (пока не остановим)
    mybot.idle()

if __name__ == "__main__":
    main()