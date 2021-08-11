from telegram.ext import MessageHandler, CommandHandler
from telegram.ext import Filters

def search(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="this is general"
    )

def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command."
    )

GENERAL_HANDLERS = [
    CommandHandler('search', search),
    MessageHandler(Filters.command, unknown),
]

#TODO: InlineQuery