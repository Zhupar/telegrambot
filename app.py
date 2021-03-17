import telebot

import config
import extensions

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты цену которой хотите узнать> \n\
<имя валюты в которой надо узнать цену первой валюты> \n\
<количество переводимой валюты> \n\
например: доллар рубль 10\n \
Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values',])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in config.KEYS.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        text = extensions.Convert.get_price(values)
    # except Exception as e:
    #     bot.reply_to(message, f"Невозможно обработать запрос")
    except extensions.APIException as e:
        bot.reply_to(message, f"{e}")
    else:
        bot.reply_to(message, text)




bot.polling()
