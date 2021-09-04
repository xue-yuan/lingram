import json
import math
import logging
import re
import os
import time

import requests

from config import config as CONFIG
from bot.utils.progressbar import Progressbar
from bot.utils.constants import Message

logger = logging.getLogger(__name__)

PAGE_SIZE = 5
TITLE_PATTERN = re.compile('[^a-zA-Z0-9]+')
STICKER_SEARCH_API = 'https://store.line.me/api/search/sticker'
STICKER_TYPE = {
    'STATIC': 0,            # 靜態貼圖
    'ANIMATION': 1,         # 動態貼圖
    'SOUND': 2,             # 音效貼圖
    'ANIMATION_SOUND': 2,   # 動態音效貼圖
    'NAME_TEXT': 3,         # 姓名貼圖
    'POPUP': 4,             # 全螢幕貼圖
    'POPUP_SOUND': 5,       # 全螢幕貼圖
    'PER_STICKER_TEXT': 6   # 訊息貼圖
}

def search(keyword: str, page: int=0) -> list:
    QUERY_PARAMS = {
        'query': keyword,
        'offset': page * PAGE_SIZE,
        'limit': PAGE_SIZE,
        'type': 'ALL',
        'includeFacets': False
    }
    COOKIES = {
        'store_lang': 'zh-hant'
    }
    
    try:
        print(1)
        request = requests.get(
            STICKER_SEARCH_API,
            params=QUERY_PARAMS,
            cookies=COOKIES
        )
        print(2)
        stickers_dict = json.loads(request.text)
        max_page = math.ceil(stickers_dict['totalCount'] / PAGE_SIZE)
        stickers_info = {
            'totalCount': stickers_dict['totalCount'],
            'items': [],
            'currentPage': page,
            'nextPage': page + 1 if page != max_page else -1,
            'previousPage': page - 1 if page != 0 else -1,
        }

        print(3)
        for sticker in stickers_dict['items']:
            stickers_info['items'].append({
                'id': sticker['id'],
                'title': sticker['title'],
                'type': STICKER_TYPE[sticker['stickerResourceType']],
            })
    except:
        raise

    return stickers_info

def download(update, context, sticker_id, message_id):
    TITLE_PATTERN = r'sticker-name-title">(.*)<'
    TITLE_SUB_PATTERN = r'[^a-zA-Z0-9]+'
    ID_PATTERN = r'id.*&quot;(.*?)&quot;,.*staticUrl'
    URL_PATTERN = r'&quot;staticUrl&quot;.*?&quot;(.*?);'

    URL = f'https://store.line.me/stickershop/product/{sticker_id}/en'

    request = requests.get(URL)
    document = request.text
    title = re.sub(TITLE_SUB_PATTERN, '_', re.search(TITLE_PATTERN, document).group(1)).strip('_ ')
    image_folder = f'{CONFIG.APP.TMP_FOLDER}/{sticker_id}'
    image_id_list = re.findall(ID_PATTERN, document)
    image_url_list = re.findall(URL_PATTERN, document)
    image_file_list = []
    length = len(image_id_list)
    progressbar = Progressbar(length, True)

    os.mkdir(image_folder)

    try:
        for id, url in zip(image_id_list, image_url_list):
            image_filename = f'{image_folder}/{id}.png'
            with open(image_filename, 'wb') as f:
                image = requests.get(url, stream=True)
                f.write(image.content) if image.status_code == 200 else exit()
                image_file_list += [image_filename]
                time.sleep(1)
            
            logger.debug(f'{image_filename} saved.')

            context.bot.editMessageText(
                chat_id=update.effective_chat.id,
                message_id=message_id,
                text=Message.PROGRESSBAR(progressbar.loading(image_id_list.index(id))),
            )

        context.bot.editMessageText(
            chat_id=update.effective_chat.id,
            message_id=message_id,
            text=Message.DOWNLOAD_SUCCESS,
        )
        
        logger.debug(f'download completely. {length} stickers in total.')
        return True, title, image_file_list

    except Exception as e:
        context.bot.editMessageText(
            chat_id=update.effective_chat.id,
            message_id=message_id,
            text=Message.DOWNLOAD_FAILED,
        )
        logger.error('error occurred while downloading the sticker.')
        logger.error(e)
        return False, None, None

