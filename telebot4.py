import telebot
from telebot import types
bot = telebot.TeleBot('5883487748:AAG1nmfdrK2X6Uj-VRR-TnAvZQAaALy5Fik')

@bot.message_handler(commands=['start'])                                                               # задаем меню
def start(message):
    markupstart = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnmenu = types.KeyboardButton('≡ Меню')
    markupstart.add(btnmenu)
    sendmessage = f'<b>Для начала работы нажмите ниже.</b>'
    bot.send_message(message.chat.id, sendmessage, parse_mode='html', reply_markup=markupstart)

@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text.strip().lower() == '≡ меню':                                                        # задаем фильмы
        markupmenu = types.InlineKeyboardMarkup(row_width=2)
        btnspider = types.InlineKeyboardButton('Человек-паук 3', callback_data='spider')
        btnmatrix = types.InlineKeyboardButton('Матрица 4', callback_data='matrix')
        btndorogaperemen = types.InlineKeyboardButton('Дорога перемен', callback_data='dorogaperemen')
        btnone = types.InlineKeyboardButton('1+1', callback_data='one')
        btnhatico = types.InlineKeyboardButton('Хатико', callback_data='hatico')
        btnbook = types.InlineKeyboardButton('Зеленая книга', callback_data='book')
        markupmenu.add(btnspider, btnmatrix, btndorogaperemen, btnone, btnhatico, btnbook)
        sendmessage = f'Добро пожаловать в меню выбора фильмов, {message.from_user.first_name}.\n' \
                      f'Выберите фильм:\n'
        bot.send_message(message.chat.id, sendmessage, parse_mode='html', reply_markup=markupmenu)

@bot.callback_query_handler(lambda call: call.data == 'spider')                                          #соответствие фильма с описанием
from DEF_file import spider

@bot.callback_query_handler(lambda call: call.data == 'matrix')
from DEF_file import matrix

@bot.callback_query_handler(lambda call: call.data == 'dorogaperemen')
from DEF_file import dorogaperemen

@bot.callback_query_handler(lambda call: call.data == 'one')
from DEF_file import one

@bot.callback_query_handler(lambda call: call.data == 'hatico')
from DEF_file import hatico

@bot.callback_query_handler(lambda call: call.data == 'book')
from DEF_file import book

bot.polling()