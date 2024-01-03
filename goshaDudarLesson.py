import telebot
bot = telebot. TeleBot('6839894064:AAEPq1qi46vGNMyM3OEY-6kVkksGJT2MDaE')
@bot. message_handler(commands=['start'])
def main (message):
    bot. send_message (message.chat.id,'Привет, семейка!')
bot.polling(none_stop=True)