import telebot
from telebot import types

bot = telebot.TeleBot('6117097971:AAEwrKYCtetbMkZnOCcC3h5EzKtLkfWBDkw')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_iser.id, "Привет! Я твой бот по Миру танков!", reply_markup=markup)

@bot.message_handler(content_types=['test'])
def det_text_messages(message):

    if message.text == 'Поздороваться':
        markyp = types.ReplyKeyboardMarkup(resize_keyboard=True) # создание новых кнопок
        btn1 = types.KeyboardButton('Новости Мира танков!')
        btn2 = types.KeyboardButton('Статистика XVM')
        markyp.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Задайте интересующий вопрос', reply_markyp=markyp) #ответ бота

    elif message.text == 'Новости Мира танков!':
        bot.send_message(message.from_user.id, 'Новости' +'[ссылке](https://tanki.su/)', parse_mode='Markdown')

    elif message.text == 'Статистика XVM!':
        bot.send_message(message.from_user.id, 'Статистика' +'[ссылке](https://modxvm.com/ru/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работа часть