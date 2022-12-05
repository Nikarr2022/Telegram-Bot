import telebot
from telebot import types
bot = telebot.TeleBot('5883487748:AAG1nmfdrK2X6Uj-VRR-TnAvZQAaALy5Fik')

@bot.message_handler(commands=['start'])                                                                   #задаем меню
def start(message):
        markupstart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnmenu = types.KeyboardButton('≡ Меню')
        markupstart.add(btnmenu)
        sendmessage = f'<b>Для начала работы нажмите ниже.</b>'
        bot.send_message(message.chat.id, sendmessage, parse_mode='html', reply_markup=markupstart)
@bot.message_handler(content_types=['text'])                                                              
def menu(message):
    if message.text.strip().lower() == '≡ меню':                                                           #задаем фильмы
        markupmenu = types.InlineKeyboardMarkup(row_width=2)
        btnspider = types.InlineKeyboardButton('Человек-паук 3', callback_data='spider')
        btnmatrix = types.InlineKeyboardButton('Матрица 4', callback_data='matrix')
        btndorogaperemen = types.InlineKeyboardButton('Дорога перемен', callback_data='dorogaperemen')
        btnone = types.InlineKeyboardButton('1+1', callback_data='one')
        markupmenu.add(btnspider, btnmatrix, btndorogaperemen,btnone)
        sendmessage = f'Добро пожаловать в меню выбора фильмов, {message.from_user.first_name}.\n' \
                      f'Выберите фильм:\n'
        bot.send_message(message.chat.id, sendmessage, parse_mode='html', reply_markup=markupmenu)
@bot.callback_query_handler(lambda call: call.data == 'spider')                                            #соответствие фильма с описанием
def spider(message):
    photo = open(r"C:\Users\79268\Downloads\Без названия.jpg", 'rb')
    msg = '<b>Человек-паук: Нет пути домой</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo=photo, caption='Рейтинг:  7.1/10\n \nОписание:\n \nПрошло пять лет с тех пор, как Питер осознал, что «с Великой силой приходит Великая ответственность!», и три года с тех пор, как он отказался быть борцом за справедливость. Но сейчас кажется, Питер прекрасно научился жить несколькими жизнями. Он хорошо учится, Нью-Йорк признал его героем, отношения с Мэри Джейн прочные. Питер даже намеревается сделать ей предложение!\n \nНо к сожалению, его лучший друг Гарри Озборн по-прежнему считает, что именно Человек-паук несет ответственность за безвременную кончину его отца. Гарри намеревается отомстить ему в образе Нового Гоблина. В то же самое время на криминальной сцене Нью-Йорка появляется другой могущественный суперзлодей, известный как Песочный Человек.\n \nКогда Человек-паук надевает таинственный черный костюм, его темная, более мстительная сторона полностью поглощает его. Эти трансформации заставляют его встретиться с самым сильным противником ― с самим собой…')
@bot.callback_query_handler(lambda call: call.data == 'matrix')
def matrix(message):
    photo = open(r"C:\Users\79268\Downloads\600x900.webp", 'rb')
    msg = '<b>Матрица: Воскрешение</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo=photo,caption='Рейтинг:  6.0/10\n \nОписание:\n \nОбычный программист Томас Андерсон по прозвищу Нео однажды узнает, что мир, в котором он живет, не реален, а сконструирован компьютерной программой под названием «Матрица». Вникая в историю «Матрицы», главный герой неожиданно для себя обнаруживает, что сам он является «избранным», чье появление сулит людям возвращение свободы.')

@bot.callback_query_handler(lambda call: call.data == 'dorogaperemen')
def dorogaperemen(message):
    photo = open(r"C:\Users\79268\Downloads\6181149-richard-yeyts-doroga-peremen.jpg", 'rb')
    msg = '<b>Дорога перемен</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo=photo,caption='Рейтинг:  7.5/10\n \nОписание:\n \nДействие картины проходит в середине 50-х годов, главные герои — члены небольшой провинциальной семьи. Фрэнк и Эйприл Уиллер считают себя семьей среднего класса, непохожей на остальные семьи, и испытывают огромное желание перебраться в Париж. Однако судьба приготовила для супругов ряд неприятных сюрпризов…')

@bot.callback_query_handler(lambda call: call.data == 'one')
def one(message):
    photo = open(r"C:\Users\79268\Downloads\Intouchables.jpg", 'rb')
    msg = '<b>1+1</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo=photo,caption='Рейтинг:  8.8/10\n \nОписание:\n \n Пострадав в результате несчастного случая, богатый аристократ Филипп нанимает в помощники человека, который менее всего подходит для этой работы, — молодого жителя предместья Дрисса, только что освободившегося из тюрьмы. Несмотря на то, что Филипп прикован к инвалидному креслу, Дриссу удается привнести в размеренную жизнь аристократа дух приключений.')

 @bot.callback_query_handler(lambda call: call.data == 'hatico')
def hatico(message):
    photo = open(r"C:\Users\79268\Downloads\982_poster_1253603681.jpg", 'rb')
    msg = '<b>Хатико</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo=photo,caption='Рейтинг:  8.3/10\n \nОписание:\n \nПрофессор университета Паркер Уилсон находит на вокзале потерявшегося щенка, отправленного из Японии в Америку. Так как за ним никто не является, Паркеру приходится оставить щенка у себя. За то время, что собака живёт у профессора, между ними возникает крепкая дружба. Паркер очень сильно привязывается к своему новому приятелю. Каждый день Хатико провожает хозяина до вокзала, когда тот отправляется на работу, а вечером приходит к вокзалу, чтобы встретить его. В один из дней профессор скоропостижно умирает на лекции в университете от сердечного приступа. Не дождавшись хозяина, Хатико продолжает приходить на станцию, не пропуская ни дня.\n До конца своих дней Хатико ежедневно приходит на станцию к прибытию поезда и ждёт до самого вечера, что вот-вот его хозяин выйдет из очередного поезда. Он так и не приходит. На этой станции преданный пёс и умирает, не дождавшись своего хозяина.')

@bot.callback_query_handler(lambda call: call.data == 'book')
def book(message):
    photo = open(r"C:\Users\79268\Downloads\Green_Book.jpg", 'rb')
    msg = '<b>Зеленая книга</b>'
    bot.send_message(message.message.chat.id, msg, parse_mode='html')
    bot.send_photo(message.message.chat.id, photo=photo,caption='Рейтинг:  8.4/10\n \nОписание:\n \nУтонченный светский лев, богатый и талантливый музыкант нанимает в качестве водителя и телохранителя человека, который менее всего подходит для этой работы. Тони «Болтун» — вышибала, не умеющий держать рот на замке и пользоваться столовыми приборами, зато он хорошо работает кулаками. Это турне навсегда изменит жизнь обоих. ')
       
        
bot.polling()
