import telebot


bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}! </b>\nВведите Фамилию или табельный номер "
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "егоров" or get_message_bot == "1627":
        final_message = f"14/06/2022 на 11 дней\nи 14/12/2022 на 14 дней"
    elif get_message_bot == "негородов" or get_message_bot == "1054":
        final_message = f"14/03/2022 на 5 дней\nи 15/08/2022 на 14 дней,\n а также 21/11/2022 на 9 дней"
    else:
        final_message = f"Попробуй ещё"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
