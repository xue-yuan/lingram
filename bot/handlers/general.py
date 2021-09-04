import json
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Update
from telegram.ext import MessageHandler, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import Filters

from bot.stickers import search_line_sticker, get_sticker
from bot.utils.emoji import emojiNum
from bot.utils.emoji import NEXT_PAGE, PREVIOUS_PAGE
from bot.utils.constants import Message

logger = logging.getLogger(__name__)
ACCEPTED_TYPE = [0, 3, 4, 6]

def __get_results_keyboard_markup(user_id, keyword, page=0):
    results = search_line_sticker(keyword, page)
    print(results)
    keyboard = [
        [InlineKeyboardButton(sticker['title'], callback_data=f'{sticker["id"]}#{sticker["type"]}#{user_id}')] for sticker in results['items']
    ]
    page_button = []

    if results["previousPage"] != -1:
       page_button.append(InlineKeyboardButton(PREVIOUS_PAGE, callback_data=f'{keyword}@{results["previousPage"]}@{user_id}'))
    page_button.append(InlineKeyboardButton(emojiNum(results["currentPage"]), callback_data='$'))
    if results["nextPage"] != -1:
       page_button.append(InlineKeyboardButton(NEXT_PAGE, callback_data=f'{keyword}@{results["nextPage"]}@{user_id}'))
    keyboard.append(page_button)

    return keyboard

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.START
    )

def search(update, context):
    try:
        if not context.args:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=Message.MISSING_ARGS
            )
        else:
            keyword = ' '.join(context.args)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=Message.SEARCH(keyword)
            )
            keyboard = __get_results_keyboard_markup(str(update.message.from_user.id), keyword)
            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(Message.SEARCH_RESULT, reply_markup=reply_markup)
    except Exception as e:
        logger.error(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Message.SEARCH_FAILED
        )

def search_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    answer = query.data

    try:
        if '#' in answer:
            # options
            sticker_id, sticker_type, user_id = answer.split('#')
            if int(sticker_type) not in ACCEPTED_TYPE:
                query.edit_message_text(text=Message.TYPE_NOT_SUPPORT)
            else:
                query.edit_message_text(text=Message.SELECTED_STICKER_ID(sticker_id))
                get_sticker(update, context, sticker_id, user_id)
        elif '@' in answer:
            # page
            keyword, page, user_id = answer.split('@')
            keyboard = __get_results_keyboard_markup(user_id, keyword, int(page))
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_reply_markup(reply_markup=reply_markup)
    except Exception as e:
        logger.error(e)
        query.edit_message_text(text=Message.SEARCH_FAILED)

def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.UNKNOWN
    )

GENERAL_HANDLERS = [
    CommandHandler('start', start),
    CommandHandler('search', search),
    CallbackQueryHandler(search_callback),
    MessageHandler(Filters.command, unknown),
]

#TODO: InlineQuery
