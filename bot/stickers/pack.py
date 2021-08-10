import logging
import os
import time

from telegram import InputFile

logger = logging.getLogger(__name__)

class StickerPack:
    def __init__(self, update, context, is_animated, name, title, images):
        self.update = update
        self.context = context
        self.is_aninated = is_animated
        self.user_id = update.effective_chat.id
        self.name = f'{name}_by_{context.bot.username}'
        self.title = f'{title}@lingram_bot'
        self.images = images

    def create_new_sticker_set(self):
        logger.debug('start to create sticker set')
        sticker_file = self.input_file(self.images[0])
        args = {
            'user_id': self.user_id,
            'name': self.name,
            'title': self.title,
            'emojis': '🍻'
        }

        if self.is_aninated:
            args['tgs_sticker'] = sticker_file
        else:
            args['png_sticker'] = sticker_file

        sticker_set_is_created = self.context.bot.create_new_sticker_set(**args)

        if sticker_set_is_created:
            logger.debug('create successfully! start to add sticker.')
            for index, image in enumerate(self.images[1:]):
                logger.debug(f'add sticker to set: {index} ')
                self.add_sticker_to_set(image)
                time.sleep(1)
        else:
            logger.debug('create failed!')

        for file in os.listdir('tmp/'):
            if file.endswith('.png'):
                os.remove(file)

        logger.debug('done.')

    def add_sticker_to_set(self, image):
        sticker_file = self.input_file(image)

        args = {
            'user_id': self.user_id,
            'name': self.name,
            'emojis': '🍻'
        }

        if self.is_aninated:
            args['tgs_sticker'] = sticker_file
        else:
            args['png_sticker'] = sticker_file

        sticker_is_added = self.context.bot.add_sticker_to_set(**args)

        if sticker_is_added:
            logger.debug('done.')
        else:
            logger.debug('error.')

    def set_sticker_set_thumb(self):
        pass

    # TODO: determine is animated
    def input_file(self, filename):
        with open(filename, 'rb') as f:
            input_file = InputFile(f, filename=filename)

        return input_file
