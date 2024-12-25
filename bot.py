#!/usr/bin/env python3
from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, filters, ContextTypes, MessageHandler, Application
import os

TOKEN: Final = '7973303768:AAG7aLAosVjPQV050zFuKzU2napJLqOu7Kk'
BOT_USERNAME: Final = '@NelsonBzo'

# This function replies to the user'
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text('Hello You!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text('I am NelsonBzo, Please type something!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text('This is a custom command')

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'How are you' in processed:
        return 'I am alright!'

    if 'python' in processed:
        return 'Remember to subscribe'

    return "I do not understand, can't respond to that."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in ({message_type}): "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
        else:
            return
    else:
        response: str = handle_response(text)
        print('Bot', response)
        await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler((CommandHandler('start', start_command)))
    app.add_handler((CommandHandler('help', help_command)))
    app.add_handler((CommandHandler('custom', custom_command)))


    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    app.run_polling(poll_interval=5)