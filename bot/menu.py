import telebot
from telebot import types

import config


start = telebot.types.ReplyKeyboardMarkup(True, False)
start.row("Еда и напитки")
start.row('Наш сайт', 'Вконтакте')
start.row('💌 О нас', '🏛 Новости')


eda_napitki = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="🍕Пицца", callback_data="Пицца")
but_2 = types.InlineKeyboardButton(text="🍱 Комбо", callback_data="Комбо")
but_3 = types.InlineKeyboardButton(text="🥨Закуски", callback_data="Закуски")
but_4 = types.InlineKeyboardButton(text="🍦Десерты", callback_data="Десерты")
but_5 = types.InlineKeyboardButton(text="🍾Напитки", callback_data="Напитки")
eda_napitki.add(but_1)
eda_napitki.add(but_2)
eda_napitki.add(but_3)
eda_napitki.add(but_4)
eda_napitki.add(but_5)


pizza1 = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(
    text="Оформить заказ", url="https://t.me/por0vos1k")
but_2 = types.InlineKeyboardButton(text="▶️", callback_data="Вперед1")
pizza1.add(but_2)
pizza1.add(but_1)


pizza2 = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="◀️", callback_data="Назад1")
but_3 = types.InlineKeyboardButton(
    text="Оформить заказ", url="https://t.me/por0vos1k")
but_2 = types.InlineKeyboardButton(text="▶️", callback_data="Вперед2")
pizza2.row(but_1, but_2)
pizza2.row(but_3)


pizza3 = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="◀️", callback_data="Назад2")
but_2 = types.InlineKeyboardButton(
    text="Оформить заказ", url="https://t.me/por0vos1k")
pizza3.add(but_1)
pizza3.add(but_2)
