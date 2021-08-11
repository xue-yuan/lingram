from bot.handlers.general import GENERAL_HANDLERS
from bot.handlers.debug import DEBUG_HANDLERS
from bot.handlers.error import ERROR_HANDLERS as _ERROR_HANDLERS
from bot.handlers.admin import ADMIN_HANDLERS as _ADMIN_HANDLERS
from config import config as CONFIG

HANDLERS = DEBUG_HANDLERS + GENERAL_HANDLERS if CONFIG.APP.DEBUG else GENERAL_HANDLERS
ERROR_HANDLERS = _ERROR_HANDLERS
ADMIN_HANDLERS = _ADMIN_HANDLERS

__all__ = (
    'HANDLERS',
    'ERROR_HANDLERS',
    'ADMIN_HANDLERS',
)
