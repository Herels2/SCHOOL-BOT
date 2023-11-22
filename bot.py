import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

ownerbot_chatid = 1027735322

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(ownerbot_chatid, 'Новый пользователь!')
    bot.send_message(ownerbot_chatid, 'ChatID:')
    bot.send_message(ownerbot_chatid, message.from_user.id)
    bot.send_message(ownerbot_chatid, 'Имя:')
    bot.send_message(ownerbot_chatid, message.from_user.first_name)
    bot.send_message(ownerbot_chatid, 'Фамилия:')
    if message.from_user.last_name == None:
        bot.send_message(ownerbot_chatid, 'Пользователь не указал фамилию')
    else:
        bot.send_message(ownerbot_chatid, message.from_user.last_name)
    bot.send_message(ownerbot_chatid, 'UserName:')
    if message.from_user.username == None:
        bot.send_message(ownerbot_chatid, 'Пользователь не указал UserName')
    else:
        bot.send_message(ownerbot_chatid, message.from_user.username)

    with open('chatids.txt', 'a+') as chatids:
        print(message.chat.id, file=chatids)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📅Расписание на завтра📅')
    item2 = types.KeyboardButton('ℹ️Информацияℹ️')
    item3 = types.KeyboardButton('👩‍🏫Учителя ведущие предметы👩‍🏫')
    item4 = types.KeyboardButton('✊🏼Тех.поддержка✊🏼')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Приветики!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['info'])
def info(message):
   bot.send_message(message.chat.id,'👨‍💻Разработчик бота: https://t.me/Sterrist 👨‍💻\n📅Дата создания бота: 22.11.2023📅\n🏫Телеграм канал школы: https://t.me/vozdvshkola 🏫')

@bot.message_handler(commands=['uroki'])
def uroki(message):
    bot.send_message(message.chat.id, '1 Урок: Русский Язык, Начало 8:15, Конец 9:00')
    bot.send_message(message.chat.id, 'Перемена 10 минут 9:00 - 9:10')
    bot.send_message(message.chat.id, '2 Урок: Русский Язык, Начало 9:10, Конец 9:55')
    bot.send_message(message.chat.id, 'Перемена 20 минут 9:55 - 10:15')
    bot.send_message(message.chat.id, '3 Урок: Русский Язык, Начало 10:15, Конец 11:00')
    bot.send_message(message.chat.id, 'Перемена 10 минут 11:00 - 11:10')
    bot.send_message(message.chat.id, '4 Урок: Русский Язык, Начало 11:10, Конец 11:55')
    bot.send_message(message.chat.id, 'Перемена 10 минут 11:55 - 12:05')
    bot.send_message(message.chat.id, '5 Урок: Русский Язык, Начало 12:05, Конец 12:50')
    bot.send_message(message.chat.id, 'Перемена 20 минут 12:50 - 13:10')
    bot.send_message(message.chat.id, '6 Урок: Русский Язык, Начало 13:10, Конец 13:55')
    bot.send_message(message.chat.id, 'Перемена 10 минут 13:55 - 14:05')
    bot.send_message(message.chat.id, '7 Урок: Русский Язык, Начало 14:05, Конец 14:50')

@bot.message_handler(commands=['teachers'])
def teachers(message):
    bot.send_message(message.chat.id,'🗨️Разговоры о важном: Малюшина Татьяна Валерьевна🗨️\n🇷🇺Русский язык: Мельникова Елена Леонидовна🇷🇺\n➕Математика: Ухова Татьяна Сергеевна➕\n🏐Физкультура: Зиновьев Сергей Викторович🏐\n🇬🇧Английский Язык: Малюшина Татьяна Валерьевна🇬🇧\n🧪Биология: Барашкова Марина Анатольевна🧪\n🎧Музыка: Воловикова Людмила Киприяновна🎧\n🖌️ИЗО: Воловикова Людмила Киприяновна🖌️\n🌍География: Кулакова Ольга Михайловна🌍\n🙋Обществознание: Малюшина Татьяна Валерьевна🙋\n📜История: Зиновьев Сергей Викторович📜\n✂️Технология: Копылова Ирина Александровна✂️\n🤷ОДНКНР: Зиновьев Сергей Викторович🤷')

@bot.message_handler(commands=['support'])
def support(message):
    bot.send_message(message.chat.id, 'https://t.me/Sterrist')

@bot.message_handler(commands=['admin'])
def admin(message):
    if message.chat.id == 1027735322:
        bot.send_message(message.chat.id, '✅Рассылка начата!✅')
        for i in open('chatids.txt', 'r').readlines():
            bot.send_message(i, 'ТЕСКТ РАССЫЛКИ')
        bot.send_message(message.chat.id, '✅Рассылка завершена!✅')
    else:
        bot.send_message(message.chat.id, 'Вы не админ!')

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':

        if message.text == '📅Расписание на завтра📅':
            bot.send_message(message.chat.id, '1 Урок: Русский Язык, Начало 8:15, Конец 9:00')
            bot.send_message(message.chat.id, 'Перемена 10 минут 9:00 - 9:10')
            bot.send_message(message.chat.id, '2 Урок: Русский Язык, Начало 9:10, Конец 9:55')
            bot.send_message(message.chat.id, 'Перемена 20 минут 9:55 - 10:15')
            bot.send_message(message.chat.id, '3 Урок: Русский Язык, Начало 10:15, Конец 11:00')
            bot.send_message(message.chat.id, 'Перемена 10 минут 11:00 - 11:10')
            bot.send_message(message.chat.id, '4 Урок: Русский Язык, Начало 11:10, Конец 11:55')
            bot.send_message(message.chat.id, 'Перемена 10 минут 11:55 - 12:05')
            bot.send_message(message.chat.id, '5 Урок: Русский Язык, Начало 12:05, Конец 12:50')
            bot.send_message(message.chat.id, 'Перемена 20 минут 12:50 - 13:10')
            bot.send_message(message.chat.id, '6 Урок: Русский Язык, Начало 13:10, Конец 13:55')
            bot.send_message(message.chat.id, 'Перемена 10 минут 13:55 - 14:05')
            bot.send_message(message.chat.id, '7 Урок: Русский Язык, Начало 14:05, Конец 14:50')

        elif message.text == 'ℹ️Информацияℹ️':
            bot.send_message(message.chat.id, '👨‍💻Разработчик бота: https://t.me/Sterrist 👨‍💻\n📅Дата создания бота: 22.11.2023📅\n🏫Телеграм канал школы: https://t.me/vozdvshkola 🏫')
        elif message.text == '👩‍🏫Учителя ведущие предметы👩‍🏫':
            bot.send_message(message.chat.id, '🗨️Разговоры о важном: Малюшина Татьяна Валерьевна🗨️\n🇷🇺Русский язык: Мельникова Елена Леонидовна🇷🇺\n➕Математика: Ухова Татьяна Сергеевна➕\n🏐Физкультура: Зиновьев Сергей Викторович🏐\n🇬🇧Английский Язык: Малюшина Татьяна Валерьевна🇬🇧\n🧪Биология: Барашкова Марина Анатольевна🧪\n🎧Музыка: Воловикова Людмила Киприяновна🎧\n🖌️ИЗО: Воловикова Людмила Киприяновна🖌️\n🌍География: Кулакова Ольга Михайловна🌍\n🙋Обществознание: Малюшина Татьяна Валерьевна🙋\n📜История: Зиновьев Сергей Викторович📜\n✂️Технология: Копылова Ирина Александровна✂️\n🤷ОДНКНР: Зиновьев Сергей Викторович🤷')
        elif message.text == '✊🏼Тех.поддержка✊🏼':
            bot.send_message(message.chat.id, 'https://t.me/Sterrist')
bot.polling(none_stop=True)