import logging

from telegram import (
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeChat,
)
from telegram.ext import Updater

from bot.commands import COMMANDS, ADMIN_COMMANDS
from bot.handlers import HANDLERS, ERROR_HANDLERS
from config import config as CONFIG

logger = logging.getLogger(__name__)

class StickerBot(Updater):
    def __set_handlers(self):
        for handler in HANDLERS:
            self.dispatcher.add_handler(handler)

        for error_handler in ERROR_HANDLERS:
            self.dispatcher.add_error_handler(error_handler)

    def __set_commands(self):
        for admin_id in CONFIG.TELEGRAM.ADMINS:
            try:
                self.bot.set_my_commands(ADMIN_COMMANDS, scope=BotCommandScopeChat(chat_id=admin_id))
            except Exception as e:
                logger.warning(e)

        self.bot.set_my_commands(COMMANDS, scope=BotCommandScopeAllPrivateChats())
        self.bot.set_my_commands(COMMANDS, scope=BotCommandScopeAllGroupChats())

    def run(self, *args, **kwargs):
        logger.info(f'start running @{self.bot.username}.')
        self.__set_handlers()
        self.__set_commands()
        if CONFIG.APP.DEBUG:
            self.start_polling(*args, **kwargs)
        else:
            self.updater.start_webhook(
                listen='0.0.0.0',
                port=CONFIG.APP.PORT,
                url_path=CONFIG.TELEGRAM.TOKEN
            )
            self.updater.bot.setWebhook(CONFIG.APP.PORT + CONFIG.TELEGRAM.TOKEN)
        self.idle()
