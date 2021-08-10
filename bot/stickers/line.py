import requests
import re
import json
import logging

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class Line:
    def __init__(self):
        pass

    def search(self):
        pass

    def download(self):
        logger.debug('start to download sticker. ID: 12165460')

        URL = 'https://store.line.me/stickershop/product/12165460/en'

        request = requests.get(URL)
        document = BeautifulSoup(request.text, 'html.parser')
        title = document.find('p', {'data-test': 'sticker-name-title'}).text
        stickers = document.select('.FnStickerPreviewItem')
        images = []
        logger.debug(f'title: {title}')

        for sticker in stickers:
            sticker_id = json.loads(sticker['data-preview'])['id']
            sticker_image = re.search(r'url\((.*)\)', str(sticker)).group(1)

            with open(f'tmp/{sticker_id}.png', 'wb') as f:
                image = requests.get(sticker_image, stream=True)
                f.write(image.content) if image.status_code == 200 else exit()

            logger.debug(f'sticker: {sticker_id} saved.')
            images += [f'tmp/{sticker_id}.png']

        logger.debug(f'download completely. {len(stickers)} stickers in total.')

        return title, title, images
