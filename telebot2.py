import telebot
from telebot import types

bot = telebot.TeleBot("5883487748:AAG1nmfdrK2X6Uj-VRR-TnAvZQAaALy5Fik")


@bot.message_handler(commands=['start'])
def start(message):
    markupstart = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnmenu = types.KeyboardButton('≡ Меню')
    markupstart.add(btnmenu)
    sendmessage = f'<b>Для начала работы нажмите ниже.</b>'
    bot.send_message(message.chat.id, sendmessage, parse_mode='html', reply_markup=markupstart)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text.strip().lower() == '≡ меню':
        markupmenu = types.InlineKeyboardMarkup(row_width=2)
        btnspider = types.InlineKeyboardButton('Человек-паук 3', callback_data='spider')
        btnmatrix = types.InlineKeyboardButton('Матрица 4', callback_data='matrix')
        markupmenu.add(btnspider, btnmatrix)
        sendmessage = f'Добро пожаловать в меню выбора фильмов, {message.from_user.first_name}.\n' \
                      f'Выберите фильм, на который хотите пойти в кино:\n'
        bot.send_message(message.chat.id, sendmessage, parse_mode='html', reply_markup=markupmenu)


@bot.callback_query_handler(lambda call: call.data == 'spider')
def spider(message):
    photo = open('spider.jpg', 'rb')
    msg = '<b>Человек-паук: Нет пути домой</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo)


@bot.callback_query_handler(lambda call: call.data == 'matrix')
def matrix(message):
    photo = open('matrix.jpg', 'rb')
    msg = '<b>Матрица: Воскрешение</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo)
bot.polling()
