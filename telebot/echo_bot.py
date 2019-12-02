import telebot


access_token = '1004359824:AAEgBBGWqb0y2eDqXyHONN6Lcf8b35Vb6Zk'
bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def echo(message):
	bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop=True)