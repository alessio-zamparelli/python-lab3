from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
from gtts import gTTS


def start(bot, update):
    # handle start on bot
    update.message.reply_text("Hello!")


def echo(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.UPLOAD_AUDIO)
    repeat_text = update.message.text
    update.message.reply_text(repeat_text)

    # convert the textual message into an mp3 file
    tts = gTTS(text=repeat_text, lang="en")
    tts.save("echo.mp3")

    # send the message back
    bot.sendVoice(update.message.chat_id, voice=open("echo.mp3", "rb"))


def main():
    """
    AmiBot will repeat everything you type

    """
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config['telegram']['token']
    updater = Updater(token
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
