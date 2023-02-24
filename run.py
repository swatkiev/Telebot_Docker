import requests
import telebot

PRIVAT_API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response = requests.get(PRIVAT_API).json()[1]

response1 = requests.get(PRIVAT_API).json()[0]

BOT_TOKEN = 'PUT HERE YOUR TOKEN FROM BOT_FATHER'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def hello_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Добрый день! Используйте команды в кавычках для управления ботом')
    bot.send_message(chat_id, 'Курс доллара на сегодня: {} /  {}.'
                              ' Введите текст "Купить доллары" или "Продать доллары" для калькуляции валют'.format(
        response['buy'] , response['sale']
    ))
    bot.send_message(chat_id, 'Курс евро на сегодня: {} /  {}.'
                              ' Введите текст "Купить евро" или "Продать евро" для калькуляции валют'.format(
        response1['buy'], response1['sale']
    ))

@bot.message_handler(content_types=['text'])
def handler_text(message):
    text = message.text
    print('Text from user - ' , text)

    if text == 'Купить доллары':
       msg = bot.send_message(message.chat.id , 'Введите сумму для покупки в $ (только цифры)')
       bot.register_next_step_handler(msg , usd , type_="sale")
    elif text == 'Продать доллары':
       msg = bot.send_message(message.chat.id , 'Введите сумму для продажи в $ (только цифры)')
       bot.register_next_step_handler(msg , usd , type_="buy")
    elif text == 'Купить евро':
        msg = bot.send_message(message.chat.id, 'Введите сумму для покупки в € (только цифры)')
        bot.register_next_step_handler(msg, eur, type_="sale")
    elif text == 'Продать евро':
        msg = bot.send_message(message.chat.id, 'Введите сумму для продажи в € (только цифры)')
        bot.register_next_step_handler(msg, eur, type_="buy")
    elif text == 'Пока':
       msg = bot.send_message(message.chat.id , 'Спасибо за обращение!')
    else:
       msg = bot.send_message(message.chat.id, 'Я Вас не понял, пожалуйста уточните свое обращение! Для управления используйте следующие команды: "/start" "Купить доллары" "Продать доллары" "Купить евро" "Продать евро" "Пока"')

def usd(message, **kwargs):
    type_ = kwargs.get('type_')
    print(type_, 'type operation')
    value = float(message.text)
    total_money = float(response[type_]) * value
    if type_ == 'sale':
        bot.send_message(message.chat.id, "Вам нужно {} грн".format(total_money))
    elif type_ == 'buy':
        bot.send_message(message.chat.id, "Вы получите {} грн".format(total_money))

def eur(message, **kwargs):
    type_ = kwargs.get('type_')
    print(type_, 'type operation')
    value = float(message.text)
    total_money = float(response1[type_]) * value
    if type_ == 'sale':
        bot.send_message(message.chat.id, "Вам нужно {} грн".format(total_money))
    elif type_ == 'buy':
        bot.send_message(message.chat.id, "Вы получите {} грн".format(total_money))

bot.polling()

print(response)
print(response1)
