# Реализовать для телеграм бота:
# Напишите программу, удаляющую из текста все слова, содержащие "абв"

import telebot

def text_clear(text, find_str):
	ch = text.split(' ')
	result = []
	for item in ch:
		if 'абв' not in item:
			result.append(item)
	if len(result) == 0:
		result = ['Empty']
	return ' '.join(result)

bot = telebot.TeleBot("5863341083:AAHVdyjHrSrqmr1fDaVB4kYSiIstMBHvPM4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	
	bot.reply_to(message, text_clear(message.text,'абв'))

bot.infinity_polling()
message: True