import telebot

# Replace 'YOUR_BOT_TOKEN' with your Telegram bot's API token
TOKEN = '7116670595:AAFDKPQxwjnrklWzuDyk9avI00ggSkAMmRc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me an Instagram Reel link, and I'll tell you how to save it.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Send me any Instagram Reel link, and I will provide instructions on how to save it legally."
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if 'instagram.com' in message.text:
        bot.reply_to(message, "To save this Reel, you can visit: https://instavideosave.net and enter the URL to download.")
    else:
        bot.reply_to(message, "Please send a valid Instagram Reel link.")

if __name__ == '__main__':
    bot.polling()
  
