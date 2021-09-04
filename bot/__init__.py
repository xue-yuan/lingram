import logging

from telegram import ParseMode
from telegram.ext import ExtBot
from telegram.ext import Defaults
from telegram.utils.request import Request

from bot import database
from bot.bot import StickerBot
from bot.utils import log
from config import config as CONFIG

logger = logging.getLogger(__name__)

stickerbot = StickerBot(
    bot=ExtBot(
        token=CONFIG.TELEGRAM.TOKEN,
        defaults=Defaults(parse_mode=ParseMode.HTML, disable_web_page_preview=True),
        request=Request(con_pool_size=8)
    ),
    use_context=True
)

def main():
    log.load_logging_config('logging.json')
    stickerbot.run(drop_pending_updates=True)
