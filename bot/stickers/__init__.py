import logging

from sqlalchemy.sql.sqltypes import Boolean

from bot import database
from bot.utils import image, clean_tmp_folder
from bot.utils.constants import Message
from bot.stickers.pack import StickerPack
from bot.stickers import line

logger = logging.getLogger(__name__)

def get_sticker(update, context, sticker_id, user_id):
    is_in_database, sticker = search_database_sticker(sticker_id)
    if is_in_database:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Message.IS_IN_DATABASE(sticker.telegram_sticker_url)
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Message.NOT_IN_DATABASE,
        )
        create_sticker(update, context, sticker_id, user_id)

def search_database_sticker(sticker_id):
    query = database.search(sticker_id)
    if query: return True, query
    return False, {}

def search_line_sticker(keyword: str, page: int=0) -> dict:
    return line.search(keyword, page)

def delete_sticker():
    pass

def create_sticker(update, context, sticker_id, user_id) -> Boolean:
    message_id = context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.DOWNLOADING
    ).message_id

    is_downloaded, title, image_file_list = line.download(update, context, sticker_id, message_id)
    if is_downloaded:
        image.resize(image_file_list)
        stickerPack = StickerPack(
            update,
            context,
            False,
            title,
            title,
            image_file_list,
            user_id
        )
        is_created = stickerPack.create_new_sticker_set()

        if is_created:
            STICKER_URL = f't.me/addstickers/{title}_by_{context.bot.username}'
            sticker = database.insert(update.effective_chat.id, title, title, STICKER_URL, sticker_id)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=Message.CREATE_SUCCESS(title, sticker.telegram_sticker_url)
            )
    clean_tmp_folder()

