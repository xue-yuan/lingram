from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters

from bot.stickers import create_sticker

def debug(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='test'
    )

def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )

def caps(update, context):
    if not context.args: return
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_caps
    )


def create(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='creating...'
    )
    create_sticker(update, context)

DEBUG_HANDLERS = [
    CommandHandler('debug', debug),
    CommandHandler('create', create),
]
