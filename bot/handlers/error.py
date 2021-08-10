import logging

logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning(f'Update `{update}` throw an exception: "{context.error}"')

ERROR_HANDLERS = [
    error
]