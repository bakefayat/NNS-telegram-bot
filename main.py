import os
import telebot
from keep_alive import keep_alive
from read_file import add_to_dictionary, list_of_products_by_code
from retrive import retrive_nns, remove_non_numerics

keep_alive()
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

novin_dictionary = add_to_dictionary()

@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    bot.send_message(message.chat.id, "بهم کد 3 رقمی محصولات نوین شرق رو بده من میگم اسمش چیه و چه شکلیه! مثلا با نوشتن 341 شروع کن")

@bot.message_handler(commands=['list'])
def send_message(message):
  msg = list_of_products_by_code()
  bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['salb'])
def send_message(message):
    bot.send_message(message.chat.id, "سلب مسئولیت: ممکن است بخشی از اطلاعات این ربات مشکل داشته باشد یا تصویر محصول و ربات مغایرت داشته باشد. هر گونه تضاد را به @ehsanbakefayat اطلاع دهید.")

@bot.message_handler()
def send_message_with_photo(message):
  request = remove_non_numerics(message.text)
  print(request)
  if request < 1000:
    msg = retrive_nns(novin_dictionary, request)
    if msg:
      photo = f'http://asbadrah.ir/tele-bot/NNS/{request}.jpg?id=2'
      bot.send_message(message.chat.id, msg)
      bot.send_photo(message.chat.id, photo)
    else:
      bot.send_message(message.chat.id, "ظاهرا چنین کدی در نوین شرق وجود ندارد.")      
  else:
    bot.send_message(message.chat.id, "ظاهرا چنین کدی در نوین شرق وجود ندارد.")

bot.polling()