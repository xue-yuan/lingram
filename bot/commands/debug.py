from telegram import BotCommand

DEBUG_COMMANDS = [
    BotCommand('debug', 'return debug message'),
    BotCommand('caps', 'return capital message'),
    BotCommand('download', 'download demo sticker'),
    BotCommand('create', 'create sticker'),
]