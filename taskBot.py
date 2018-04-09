from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


"""

/showTasks
/newTask	<task	to	add>
/removeTask	<task	to	remove>
/removeAllTasks	<substring	to	use	to	remove	all	the	tasks	that	contain	it>


"""


def showTasks(bot, update):


def newTask(bot, update):


def removeTask(bot, update):


def removeAllTasks(bot, update):


def main():

    updater = Updater("541907262:AAEOOVHWPnGZPJcHjHEkVtvsJ_asrRdwc14")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask))
    dp.add_handler(CommandHandler("removeTask", removeTask))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks))

    updater.start_polling()
    updater.idle()


def start(bot, update):
    # handle start on bot
    update.message.reply_text("connected")


if __name__ == "__main__":
    main()
