import telebot
from rembg import remove
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'hi'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)



@bot.message_handler(content_types=['photo'])
def clear_background(m):
	file_path = bot.get_file(m.photo[-1].file_id).file_path
	photo = bot.download_file(file_path)
	#photo = remove(photo)
	bot.send_photo(m.chat.id, photo)

bot.polling(none_stop=True, interval=0)

