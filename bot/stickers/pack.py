import logging
import os
import time
from sqlalchemy.sql.sqltypes import Boolean

from telegram import InputFile
from bot.utils.constants import Message
from bot.utils.progressbar import Progressbar

logger = logging.getLogger(__name__)

class StickerPack:
    def __init__(self, update, context, is_animated, name, title, image_file_list, user_id):
        self.update = update
        self.context = context
        self.is_aninated = is_animated
        self.user_id = user_id
        self.name = f'{name}_by_{context.bot.username}'
        self.title = f'{title}@{context.bot.username}'
        self.images = image_file_list

    def create_new_sticker_set(self) -> Boolean:
        sticker_file = self.input_file(self.images[0])
        length = len(self.images[1:])
        args = {
            'user_id': self.user_id,
            'name': self.name,
            'title': self.title,
            'emojis': '🍻'
        }

        if self.is_aninated: args['tgs_sticker'] = sticker_file
        else: args['png_sticker'] = sticker_file

        sticker_set_is_created = self.context.bot.create_new_sticker_set(**args)

        try:
            if sticker_set_is_created:
                progressbar = Progressbar(length, True)
                message_id = self.context.bot.send_message(
                    chat_id=self.update.effective_chat.id,
                    text=Message.MAKING,
                ).message_id

                for index, image in enumerate(self.images[1:]):
                    logger.debug(f'add sticker to set: {index} ')
                    self.add_sticker_to_set(image)
                    self.context.bot.editMessageText(
                        chat_id=self.update.effective_chat.id,
                        message_id=message_id,
                        text=Message.PROGRESSBAR(progressbar.loading(index))
                    )
                    time.sleep(1)
                
                self.context.bot.editMessageText(
                    chat_id=self.update.effective_chat.id,
                    message_id=message_id,
                    text=Message.MAKE_SUCCESS,
                )
                return True
            else:
                self.context.bot.send_message(
                    chat_id=self.update.effective_chat.id,
                    text=Message.MAKE_FAILED,
                )
                logger.error('sticker has already existed!')
                return False
        except Exception as e:
            self.context.bot.send_message(
                chat_id=self.update.effective_chat.id,
                text=Message.MAKE_FAILED,
            )
            logger.error('create failed!')
            logger.error(e)
            return False

    def add_sticker_to_set(self, image):
        sticker_file = self.input_file(image)

        args = {
            'user_id': self.user_id,
            'name': self.name,
            'emojis': '🍻'
        }

        if self.is_aninated: args['tgs_sticker'] = sticker_file
        else: args['png_sticker'] = sticker_file

        sticker_is_added = self.context.bot.add_sticker_to_set(**args)
        
        if not sticker_is_added:
            raise Exception("Add Failed")

    # TODO: determine is animated
    def input_file(self, filename):
        with open(filename, 'rb') as f:
            input_file = InputFile(f, filename=filename)

        return input_file
