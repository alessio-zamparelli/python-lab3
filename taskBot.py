from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
tasks_list = list()


"""

/showTasks
/newTask	<task	to	add>
/removeTask	<task	to	remove>
/removeAllTasks	<substring	to	use	to	remove	all	the	tasks	that	contain	it>


"""


def load_list(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            tasks_list.append(line.strip())


def save_list(path):
    f = open(path, 'w')
    for item in tasks_list:
        f.write("%s\n" % item)


def showTasks(bot, update):
    if len(tasks_list) == 0:
        update.message.reply_text("no tasks memorized yet")
        return
    tasks_list.sort()
    for element in tasks_list:
        update.message.reply_text(element)


def newTask(bot, update):
    print("What?")
    new_task = input()
    tasks_list.append(new_task)


def removeTask(bot, update):
    print("Write the item to delete")
    to_be_deleted = input()
    try:
        tasks_list.remove(to_be_deleted)
    except ValueError:
        print("element not found!")


def removeAllTasks(bot, update):


def start(bot, update):
    # handle start on bot
    update.message.reply_text("connected")


def main():
    pathToFile = "/home/ale-dell/PycharmProjects/python-lab2/task_list.txt"

    updater = Updater("541907262:AAEOOVHWPnGZPJcHjHEkVtvsJ_asrRdwc14")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask))
    dp.add_handler(CommandHandler("removeTask", removeTask))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks))

    load_list(pathToFile)
    save_list(pathToFile)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
