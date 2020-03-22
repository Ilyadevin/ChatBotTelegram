import telebot
from Directories.Translation_YA.translation import *

bot = telebot.TeleBot('YourTelegramAPI')
mode = 0
lang = 'ru'
statusd = 'close'
statusw = 'close'
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard.row('Help', 'Настройки', 'meeting')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! С чего начнем? /help')


@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.chat.id, 'Я - бот который поможет вам облегчить жизнь в контексте некоторых задач.\n'
                                      'Сейчас я умею переводить тексты на нужный вам язык.\n'
                                      'Но пока что, к сожалению не все на свете ;)\n'
                                      'Команды - "Настроки", "translate"\n')


@bot.message_handler(content_types=['text'])
def meeting_app(message):
    bot.send_message(message.chat.id, 'У меня есть одна экспериментальная функция!\n'
                                      'Я могу найти тебе собеседника по интересам, но к сожалению, '
                                      'не в телеграмме.\n '
                     )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global mode, lang
    if message.text.lower() == 'translate' or message.text.lower == '/translate':
        bot.send_message(message.from_user.id, 'Привет ещё раз ;)\n'
                                               'Я бот - который переводит слова и тексты,\n'
                                               'напиши мне что ты хочешь перевести и я сделаю это!\n'
                                               'Переведено сервисом "Яндекс.Переводчик" - https://translate.yandex.ru\n'
                                               'Чтобы настроить перевод, используйте, пожалуйста - настройки\n')
    elif message.text.lower() == 'настройки':
        bot.send_message(message.from_user.id, 'Перевод работает на нескольких языках, выберите на какой перевеодить\n'
                                               'Доступные на данный момент: en, ru, uk(Украинский), is.\n'
                                               'Введите один из них.\n')
        mode = 1
    elif message.text.lower() == 'meeting' or message.text.lower == '/meeting':
        meeting_app(message.text)
    elif mode == 1 and message.text.lower() == 'en' \
            or mode == 1 and message.text.lower() == 'is' \
            or mode == 1 and message.text.lower() == 'ru' \
            or mode == 1 and message.text.lower() == 'uk':
        bot.send_message(message.from_user.id, f'Переключаю на {message.text.lower()}')
        lang = message.text.lower()
        mode = 0
    elif mode == 1 and message.text.lower() != 'en' \
            or mode == 1 and message.text.lower() != 'ru' \
            or mode == 1 and message.text.lower() != 'uk' \
            or mode == 1 and message.text.lower() != 'is':
        bot.send_message(message.from_user.id, 'Я не понял твой язык, введите другой.\n '
                                               'ПОДДЕРЖИВАЕМЫЕ язык - en, ru, uk(Украинский), is.\n')
    else:
        bot.send_message(
            message.from_user.id, f'Ваш перевод - {get_translate(message.text.lower(), lang)["text"]}\n'
                                  f' переведено сервисом "Яндекс.Переводчик" - https://translate.yandex.ru'
        )
        bot.send_message(message.from_user.id, f'Сейчас я использую {lang}.\n'
                                               f'Если вы хотите изменить язык используйте - настройки.\n')


bot.polling(none_stop=True)
