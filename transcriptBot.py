# ------------------------------
# File          : transcriptBot.py
# Author        : Kevin Manca (github.com/kevinm6)
# Date          : 28/02/2023, 11:51
# ------------------------------
#
# Description:
# This is a simple Python Bot that aims to transcript voice messages
# using GoogleAPI for audio recognition
#
# Requirements:
#   - Token generate with BotFather (t.me/botfather)
#   - Python >= 3
#   - requirements.txt (`pip install -r requirements.txt`)
#
# Usage:
#   - create a file named `token` and put in the same directory of this bot
#   - run the bot with `python transcriptBot.py`

import os
# import logging
# import datetime
from telegram import Update
from telegram.ext import (
        Application,
        CommandHandler,
        ContextTypes,
        MessageHandler,
        filters
)

idle = False

# Disable logging for now
# logfile = "/var/log/tg_bot/" + str(datetime.date.today()) + ".log"
# logging.basicConfig(
        #         format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
        #         )
# logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    global idle
    idle = False

    await update.message.reply_text(text = f"▶️  Hi {update.effective_user.mention_markdown()}, starting the *Bot*\!",
                                    parse_mode = "MarkdownV2",
                                    reply_to_message_id = update.message.id)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global idle

    if not idle:
        """Send a message when the command /help is issued."""
        await update.message.reply_text(text="""
🎙 *Audio2Text Bot*

I'll try to transcript voice message to text,
tested only with Italian and English\.""",
                                        parse_mode="MarkdownV2",
                                        reply_to_message_id=update.message.id)

async def transcript_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not idle:
        import speech_recognition as sr
        from pydub import AudioSegment

        message = update.message
        # get basic info about the voice note file and prepare it for downloading
        try:
            """Started recognition..."""

            # file_info = context.bot.get_file(message.voice.file_id)
            # print ("file_id: " + str(message.voice.file_id))
            dirPath = r"/tmp/telegram_bot/voice_msgs/"
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            new_file = await context.bot.get_file(update.message.voice.file_id)
            # download the voice message as a file
            file_name=f"vmsg_{message.voice.file_unique_id}"
            await new_file.download_to_drive(f"{dirPath}/{file_name}.ogg")

            AudioSegment.from_ogg(f"{dirPath}/{file_name}.ogg").export(f"{dirPath}/{file_name}.wav", format = 'wav')
            audio_recognizer = sr.Recognizer()

            with sr.AudioFile(f"{dirPath}/{file_name}.wav") as voice_wav:
                audio_data = audio_recognizer.record(voice_wav)

                # text result from Google
                language_user_code = "it"
                result_text = audio_recognizer.recognize_google(audio_data,
                                                                language = language_user_code if language_user_code != None else "it-IT")

                # Send confirmation to user as a message
                await message.reply_text(text = f"💬 *Transcription Result*:\n\n`{result_text}`",
                                         parse_mode="MarkdownV2",
                                         reply_to_message_id = message.id)

            # remove files after send
            files = [ f"{dirPath}/{file_name}.ogg", f"{dirPath}/{file_name}.wav" ]
            for file in files:
                if os.path.isfile(file):
                    try:
                        os.remove(file)
                    except os.error as err:
                        print(err)


        except sr.UnknownValueError as e:
            await message.reply_text(text = "I don't get the voice message, be more clear!\n I'm sure the message was from Saba",
                                     reply_to_message_id = message.id)
            print(e)
            # with open(logfile, 'a', encoding='utf-8') as f:
            #     f.write(str(datetime.datetime.today().strftime("%H:%M:%S")) + ':' + str(message.from_user.id) + ':' + str(message.from_user.first_name) + '_' + str(message.from_user.last_name) + ':' + str(message.from_user.username) +':'+ str(message.from_user.language_code) + ':Message is empty.\n')

        except Exception as e:
            await message.reply_text(text = """\
                    Something went wrong, but our brave engineers are already working on a solution...
    FUCK, I'm just kidding! 😃
    Come on, no one will fix this error, it will just get lost in the logs.
    Funny, I've disable logging.""",
                                     reply_to_message_id = message.id)
            print(e)

            # with open(logfile, 'a', encoding='utf-8') as f:
            #     f.write(str(datetime.datetime.today().strftime("%H:%M:%S")) +
            #      ':' + str(message.from_user.id) + ':' +
            #      str(message.from_user.first_name) + '_' +
            #      str(message.from_user.last_name) + ':' + str(message.from_user.username) +
            #      ':'  str(message.from_user.language_code) +':' + str(e) + '\n')


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    global idle
    idle = True
    await update.message.reply_text(
            f"Stopped Bot!",
            reply_to_message_id = update.message.id)


def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    # If you don't have a token, generate it with BotFather (t.me/botfather)
    with open("/Users/Kevin/dev/audioToText-bot/token") as t:
        API_TOKEN = t.read().rstrip()
    application = Application.builder().token(API_TOKEN).build()

    # handle default commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stop", stop))

    application.add_handler(MessageHandler(filters.VOICE, transcript_voice_message))

    # Run the bot-loop until <C-c>
    application.run_polling()

if __name__ == '__main__':
    main()
