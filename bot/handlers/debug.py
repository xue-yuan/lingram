from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters

from bot.stickers import download_sticker, pack

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

def download(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='downloading...'
    )
    download_sticker()

def create(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='creating...'
    )
    pack(update, context)

DEBUG_HANDLERS = [
    CommandHandler('debug', debug),
    CommandHandler('caps', caps),
    CommandHandler('download', download),
    CommandHandler('create', create),
    MessageHandler(Filters.text & (~Filters.command), echo),
]
