from bot.commands.general import GENERAL_COMMANDS
from bot.commands.debug import DEBUG_COMMANDS
from bot.commands.admin import ADMIN_COMMANDS as _ADMIN_COMMANDS
from config import config as CONFIG

COMMANDS = DEBUG_COMMANDS + GENERAL_COMMANDS if CONFIG.APP.DEBUG else GENERAL_COMMANDS
ADMIN_COMMANDS = _ADMIN_COMMANDS + COMMANDS

__all__ = (
    'COMMANDS',
    'ADMIN_COMMANDS',
)
