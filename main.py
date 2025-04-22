from telegram.ext import Updater, CommandHandler,MessageHandler
from telegram import Update
from config import bot_token , contac, greet

def start(update,context): update.message.reply_text(greet())














def main():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))


if __name__ == '__main__':
    main()