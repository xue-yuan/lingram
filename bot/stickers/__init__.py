import logging

from bot.stickers.pack import StickerPack
from bot.stickers.line import Line
from bot.utils import image

logger = logging.getLogger(__name__)

def search_sticker():
    # search database then search line
    pass

def list_sticker():
    pass

def download_sticker():
    # download()
    pass

def delete_sticker():
    pass

def pack(update, context):
    line = Line()
    name, title, images = line.download()
    image.resize(images)
    stickerPack = StickerPack(
        update,
        context,
        False,
        name.replace(' ', '_'),
        title,
        images
    )
    stickerPack.create_new_sticker_set()
