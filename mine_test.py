#import asyncio
#from aiogram.types import Message
#import config
#from aiogram import Bot, types
#from aiogram.dispatcher import Dispatcher
#from aiogram.utils import executor
#from aiogram.types import ReplyKeyboardMarkup
#from aiogram.types import InlineKeyboardMarkup
#from aiogram.types import InlineKeyboardButton


import config
import telebot
from telebot import types



start = telebot.types.ReplyKeyboardMarkup(True, False)
start.row('🗂 Каталог товаров')
start.add('Работа с RatHouse', '💼 Контакты')
start.row('💌 Отзывы', '🏛 Новости')



admibro = telebot.types.ReplyKeyboardMarkup(True, False)
admibro.row('🗂 Каталог товаров')
admibro.add('🔥АДМИН ПАНЕЛЬ🔥')
admibro.add('Работа с RatHouse', '💼 Контакты')
admibro.row('💌 Отзывы', '🏛 Новости')


abc = telebot.types.ReplyKeyboardMarkup(True, False)
abc.row('💰Баланс', '📈Статистика', '🛠Настройка ассортимента')
abc.row('😈Админы', '🛒Добавить товар', '💲Настройка платежек')
abc.row('📩Рассылка', '🦋Стикеры', '💻Настройка ответов бота')
abc.row('🤴Работники', '⛔️Черный список', '🙎‍♂️Пользователи')
abc.add('⬅️ Назад')


krekin = telebot.types.ReplyKeyboardMarkup(True, False)
krekin.row('Отправить новое сообщение')
krekin.row('⬅️ Назад')



keyboard = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="💰Деньги", callback_data="💳 Деньги")
but_2 = types.InlineKeyboardButton(text="🧨Схемы", callback_data="📚Схемы")
but_3 = types.InlineKeyboardButton(text="🛒Услуги", callback_data="🛒Услуги")
but_4 = types.InlineKeyboardButton(text="🗂Обучение", callback_data="🗂Обучение")
but_5 = types.InlineKeyboardButton(text="🎮Аккаунты", callback_data="🎮Аккаунты")
but_6 = types.InlineKeyboardButton(text="🍔Еда за 40%", callback_data="🍔Еда за 40%")
#but_7 = types.InlineKeyboardButton(text="📎Товары", callback_data="📎Товары")
but_8 = types.InlineKeyboardButton(text="😈Софт", callback_data="😈Софт")
keyboard.row(but_1, but_2)
keyboard.row(but_6, but_5)
keyboard.row(but_4, but_8)
keyboard.row(but_3)



ret = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="GOOGLE DRIVE UNLIMITED", callback_data="GOOGLE DRIVE UNLIMITED")
but_2 = types.InlineKeyboardButton(text="Софт Магнита", callback_data="Софт Магнита")
but_3 = types.InlineKeyboardButton(text="Adobe Photoshop", callback_data="Adobe Photoshop")
but_4 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
ret.row(but_1)
ret.row(but_2)
ret.row(but_3)
ret.row(but_4)



rich = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Qiwi", callback_data="Qiwi")
but_2 = types.InlineKeyboardButton(text="ЯД/Юмани", callback_data="ЯД/Юмани")
but_3 = types.InlineKeyboardButton(text="BTC", callback_data="BTC")
but_4 = types.InlineKeyboardButton(text="Физ. карты", callback_data="Физ. карты")
but_5 = types.InlineKeyboardButton(text="PAYEER", callback_data="PAYEER")
but_6 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
rich.row(but_1)
rich.row(but_2)
rich.row(but_3)
rich.row(but_4)
rich.row(but_5)
rich.row(but_6)



typer = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="МУЗЫКА, БИТЫ", callback_data="МУЗЫКА, БИТЫ")
but_2 = types.InlineKeyboardButton(text="3D МОДЕЛИРОВАНИЕ", callback_data="3D МОДЕЛИРОВАНИЕ")
but_3 = types.InlineKeyboardButton(text="РАЗРАБОТКА ИГР", callback_data="РАЗРАБОТКА ИГР")
but_4 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
typer.row(but_1)
typer.row(but_2)
typer.row(but_3)
typer.row(but_4)



linux = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="🍟Макдональдс", callback_data="🍟Макдональдс")
but_2 = types.InlineKeyboardButton(text="🍦Бургер Кинг", callback_data="🍦Бургер Кинг")
but_3 = types.InlineKeyboardButton(text="🧲Магнит", callback_data="🧲Магнит")
but_4 = types.InlineKeyboardButton(text="♻️Пятерочка", callback_data="♻️Пятерочка")
but_5 = types.InlineKeyboardButton(text="🍕Яндекс", callback_data="🍕Яндекс")
but_6 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
linux.row(but_1)
linux.row(but_2)
linux.row(but_3)
linux.row(but_4)
linux.row(but_5)
linux.row(but_6)



tovar = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="📱Анонимный телефон", callback_data="📱Анонимный телефон")
but_2 = types.InlineKeyboardButton(text="💻 Анонимный ноутбук", callback_data="💻 Анонимный ноутбук")
but_3 = types.InlineKeyboardButton(text="🕹 Анонимная флешка", callback_data="🕹 Анонимная флешка")
but_4 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
tovar.row(but_1)
tovar.row(but_2)
tovar.row(but_3)
tovar.row(but_4)




rend = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Avito (пустой)", callback_data="Avito (пустой)")
but_2 = types.InlineKeyboardButton(text="Avito (раскрученный)", callback_data="Avito (раскрученный)")
but_3 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
rend.row(but_1)
rend.row(but_2)
rend.row(but_3)



gopa = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Aвито", callback_data="Авито")
but_2 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
gopa.row(but_1)
gopa.row(but_2)



koret = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="📵 Телефон", callback_data="Мтс")
but_2 = types.InlineKeyboardButton(text="🚕 Возврат такси", callback_data="Возврат денег за такси")
but_3 = types.InlineKeyboardButton(text="📈 Соц.сети", callback_data="Накрутка")
but_4 = types.InlineKeyboardButton(text="👔 Шмотки", callback_data="Бренд")
but_5 = types.InlineKeyboardButton(text="📱Пробив", callback_data="Пробив")
but_6 = types.InlineKeyboardButton(text="💻 Программист", callback_data="💻 Программист")
but_7 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="Назад101")
but_8 = types.InlineKeyboardButton(text="🔫 REFUND", callback_data="Реф")
but_9 = types.InlineKeyboardButton(text="🖌Дизайн", callback_data="🖌Дизайн")
koret.row(but_5, but_2)
koret.row(but_4, but_6)
koret.row(but_1, but_3)
koret.row(but_9, but_8)
koret.row(but_7)


zxc = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="[Пассив] Зарабатываем с помощью Instagram", callback_data="Instagram")
but_2 = types.InlineKeyboardButton(text="Скам фортнайт", callback_data="Скам фортнайт")
but_3 = types.InlineKeyboardButton(text="Аккаунты Facebook", callback_data="Аккаунты Facebook")
but_4 = types.InlineKeyboardButton(text="Схема VK 2020 (PREMIUM)", callback_data="Схема VK 2020 (PREMIUM)")
but_5 = types.InlineKeyboardButton(text="Посредничество на фрилансе", callback_data="Посредничество на фрилансе")
but_6 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад")
zxc.row(but_2)
zxc.row(but_3)
zxc.row(but_4)
zxc.row(but_5)
zxc.row(but_1)
zxc.row(but_6)




oplati = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Оплатить", url="https://t.me/por0vos1k")
but_2 = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="Назад")
oplati.row(but_1)
oplati.row(but_2)

svize = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Связаться", url=config.svize)
svize.row(but_1)



money_cash = telebot.types.ReplyKeyboardMarkup(True, False)
money_cash.row('Qiwi')
money_cash.row('Яндекс Деньги')
money_cash.row('Bitcoin')
money_cash.add('⬅️ Назад')


nice = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Узнать настройки", callback_data="Узнать настройки")
nice.row(but_1)

