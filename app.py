# - *- coding: utf- 8 - *-

#Production by Berlin
#Telegram - @por0vos1k


import telebot
import time
from datetime import datetime
import random
import menu
import urllib
import config
from io import BytesIO
from telebot import types


bot = telebot.TeleBot(config.token, parse_mode=None)
print("Start")


joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(str(message.chat.id))
        bot.send_message(message.chat.id, "Сеть пиццерий №1 в России.\n\nЗаказать пиццу можно через сайт dodopizza.ru или в приложении: dodopizza.onelink.me/YlkM/vksmm\n\nДодо Пицца — международная сеть пиццерий, которая родилась в Сыктывкаре, а работает уже в тринадцати странах мира. Обычно люди приходят в Додо Пиццу, чтобы просто поесть. Но для нас Додо — не только пицца, а большое дело, которое вдохновляет, заставляет каждое утро просыпаться и с интересом продолжать работу.\n\nМы создаём инновационную компанию из России на основе принципа полной открытости. Не боимся признавать ошибки и делиться успехами с вами. Но наша главная цель — доставлять вам самую вкусную пиццу максимально быстро.", reply_markup=menu.start)
    else:
        bot.send_message(message.chat.id, "Сеть пиццерий №1 в России.\n\nЗаказать пиццу можно через сайт dodopizza.ru или в приложении: dodopizza.onelink.me/YlkM/vksmm\n\nДодо Пицца — международная сеть пиццерий, которая родилась в Сыктывкаре, а работает уже в тринадцати странах мира. Обычно люди приходят в Додо Пиццу, чтобы просто поесть. Но для нас Додо — не только пицца, а большое дело, которое вдохновляет, заставляет каждое утро просыпаться и с интересом продолжать работу.\n\nМы создаём инновационную компанию из России на основе принципа полной открытости. Не боимся признавать ошибки и делиться успехами с вами. Но наша главная цель — доставлять вам самую вкусную пиццу максимально быстро.", reply_markup=menu.start)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'Пицца':
            url = 'https://telegra.ph/dodo-2077-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Додо 2077</a>\n\nИнгредиенты: Пицца 30 см, соус киберкола барбекю, бекон, митболы из говядины, пикантная пепперони, томаты черри, моцарелла, шампиньоны, сладкий перец, красный лук, чеснок, томатный соус\n\nЦена: 745 руб.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza1)
        elif call.data == 'Вперед1':
            url = 'https://telegra.ph/dodo-fresh-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Пепперони фреш</a>\n\nИнгредиенты: 30 см, традиционное тесто, 610 г, Пикантная пепперони, увеличенная порция моцареллы, томаты, томатный соус\n\nЦена: 435 руб.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza2)
        elif call.data == 'Назад1':
            url = 'https://telegra.ph/dodo-2077-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Додо 2077</a>\n\nИнгредиенты: Пицца 30 см, соус киберкола барбекю, бекон, митболы из говядины, пикантная пепперони, томаты черри, моцарелла, шампиньоны, сладкий перец, красный лук, чеснок, томатный соус\n\nЦена: 745 руб.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza1)
        elif call.data == 'Вперед2':
            url = 'https://telegra.ph/dodo-peperoni-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Пепперони</a>\n\nИнгредиенты: 30 см, традиционное тесто, 570 г, Пикантная пепперони, увеличенная порция моцареллы, томатный соус\n\nЦена: 625 руб.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza3)
        elif call.data == 'Назад2':
            url = 'https://telegra.ph/dodo-fresh-01-02'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<a href='{}'>Пепперони фреш</a>\n\nИнгредиенты: 30 см, традиционное тесто, 610 г, Пикантная пепперони, увеличенная порция моцареллы, томаты, томатный соус\n\nЦена: 435 руб.".format(url), parse_mode='HTML')
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=menu.pizza2)
        elif call.data == 'Комбо':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Закуски':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Десерты':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Напитки':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        else:
            bot.send_message(call.message.chat.id, "Ничего не понятно!")



@bot.message_handler(content_types=["text"])
def send(message):
    if message.text == 'Еда и напитки':
        bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=menu.eda_napitki)
    elif message.text == '💌 О нас':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Читать дальше", url="https://dodopizza.ru/moscow/about")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "💌 О нас\n\nНо для нас Додо — не только пицца. Это и пицца тоже, но в первую очередь это большое дело, которое вдохновляет нас, заставляет каждое утро просыпаться и...", reply_markup=keyboard)
    elif message.text == 'Наш сайт':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://dodopizza.ru")
        keyboard.add(url_button)
        photo = open('huthgutgh.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=keyboard)
    elif message.text == 'Вконтакте':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Перейти по ссылке', url='https://vk.com/dodo')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "❤️Мы появились Вконтакте", reply_markup=keyboard)
    elif message.text == '🏛 Новости':
        photo = open('novosti_dodo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='15 топовых призов 🤩\n\nСегодня Найт-Сити распахнул свои двери для всех желающих, а мы запускаем киберконкурс! Разыгрываем крутой мерч от Cyberpunk 2077: 10 футболок, 4 бомбера и приставку Xbox Series X в комплекте с игрой.\n\nЧто нужно сделать:\n1. Закажите пиццу Додо 2077.\n2. Найдите в нашем Инстаграмм аккаунте (https://www.instagram.com/dodopizza/) Insta-маску Додо 2077. Наведите ее на коробку пиццы и сделайте фото/видео киберголограммы.\n3. Выложите это в stories.\n4. Отметьте @dodopizza.\n\nИтоги подведем 26 декабря в прямом эфире с помощью рандомайзера. Открытый аккаунт в Instagram — обязательное условие. Всем удачи!\n\nПодробные правила проведения акции — https://vk.cc/bVOsIv')
    else:
        bot.send_message(message.chat.id, "Ничего не понятно!")



#Start Bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
