from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters

def clear(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='test'
    )

def whois(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='admin'
    )

ADMIN_HANDLERS = [
    CommandHandler('clear', clear),
    CommandHandler('whois', whois),
]