import logging

logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning(f'Exception: "{context.error}"')

ERROR_HANDLERS = [
    error
]