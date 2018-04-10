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
    update.message.reply_text("What?")
    task_to_be_added = bot.text
    print(task_to_be_added)
    tasks_list.append(task_to_be_added)
    showTasks()
    update.message.reply_text("added" + task_to_be_added)


def removeTask(bot, update):
    update.message.reply_text("Write the item to delete")

    to_be_deleted = update.message.text
    try:
        tasks_list.remove(to_be_deleted)
    except ValueError:
        update.message.reply_text("element not found!")


def removeAllTasks(bot, update):
        update.message.reply_text("not implemented yet")


def start(bot, update):
    # handle start on bot
    update.message.reply_text("connected")
    update.message.reply_text(
        "list of commands:\n/show_tasks\tshow all saved tasks\n/new_tasks\tadd a new task\n/remove_task\n/remove_all_tasks\tremove all tasks\nsave_tasks\tsave current list")


def testPrint():
    if len(tasks_list) == 0:
        print("no tasks memorized yet")
        return
    tasks_list.sort()
    print(*tasks_list, sep='\n')


def main():
    pathToFile = "/home/ale-dell/PycharmProjects/python-lab2/task_list.txt"

    updater = Updater("541907262:AAEOOVHWPnGZPJcHjHEkVtvsJ_asrRdwc14")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("show_tasks", showTasks))
    dispatcher.add_handler(CommandHandler("new_task", newTask))
    dispatcher.add_handler(CommandHandler("remove_task", removeTask))
    dispatcher.add_handler(CommandHandler("remove_all_tasks", removeAllTasks))
    dispatcher.add_handler(CommandHandler("save_tasks", save_list))

    load_list(pathToFile)

    # testPrint()

    updater.start_polling()
    updater.idle()

    # save_list(pathToFile)


if __name__ == "__main__":
    main()
