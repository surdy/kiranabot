from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes 
from kirana import read_list, add_to_list, remove_from_list
import os

#\u2705 
TOKEN: Final = os.environ['BOT_TOKEN']


HELP_TEXT = """``` I am Kirana Bot. I can add items to your Grocery list
 Here are a few things you can do:
    <item>    Enter an item to be added to the list
    /help     Show this help text
    /list     List items in the grocery list```"""

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello !! Thanks for chatting with me! I am Kirana bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, parse_mode='MarkdownV2')

async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for item in list_items:
        keyboard = keyboard + [[InlineKeyboardButton(item, callback_data=item)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text='Here is the list:', reply_markup=reply_markup)


# Handlers

def handle_response(text: str) -> str:
    processed: str = text.lower()

    add_to_list(processed)
    reply = processed + ' added to the list'
    return reply


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.first_name} at {update.message.date}: "{text}"')

    response: str= handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':

    list_items = read_list()

    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('list', list_command))


    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
