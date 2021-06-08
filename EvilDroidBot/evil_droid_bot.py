# Evil Droid Bot

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import settings


def greet_user(update: Update, context: CallbackContext):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text)

def main():
	mybot = Updater(settings.API_KEY)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))

	mybot.start_polling()
	mybot.idle()

main()