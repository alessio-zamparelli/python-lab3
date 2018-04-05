from telegram.ext import Updater


def start():
    #handle start on bot



def main():
    """
    AmiBot will repeat everything you type

    """
    updater = Updater("541907262:AAEOOVHWPnGZPJcHjHEkVtvsJ_asrRdwc14")
    updater.start_polling()
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

if __name__ == '__name__':
    main()