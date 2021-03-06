class Message():

    START="""
    ðº æ­¡è¿ä½¿ç¨ @lingrambotï¼è¼¸å¥ / å¯ä»¥æ¥çå¯ç¨æä»¤ãæä»»ä½åé¡å¯ä»¥ä¸ <a href="https://github.com/xue-yuan/lingram">GitHub</a> è·æåæã
    """

    SEARCH_RESULT = 'â¨ æå°çµæ'
    DOWNLOADING = 'ð  ä¸è¼ä¸­'
    DOWNLOAD_SUCCESS = 'ð  ä¸è¼å®ç¢'
    MAKING = 'ð  è£½ä½ä¸­'
    MAKE_SUCCESS = 'ð  è£½ä½å®ç¢'
    NOT_IN_DATABASE = 'ð¡ è³æåº«ç¡è²¼åè³è¨ï¼è£½ä½æéç´ 2 åé'

    DOWNLOAD_FAILED = 'â ä¸è¼å¤±æï¼è«éæ°æä½'
    MAKE_FAILED = 'â è£½ä½å¤±æï¼è«éæ°æä½'
    SEARCH_FAILED = 'â æå°å¤±æï¼è«éæ°æä½'
    TYPE_NOT_SUPPORT = 'â è²¼åé¡åç®åä¸æ¯æ´'
    UNKNOWN = "â Sorry, I didn't understand that command"
    MISSING_ARGS = 'â Missing keyword(s)'

    @staticmethod
    def IS_IN_DATABASE(url):
        return f'â è²¼åå­å¨æ¼è³æåº«ï¼<a href="{url}">é»ææ°å¢</a>'

    @staticmethod
    def CREATE_SUCCESS(title, url):
        return f'â¡ï¸ é»ææ°å¢ <a href="{url}">{title}</a>'

    @staticmethod
    def SEARCH(title):
        return f'ð æå° <b>{title}</b>'

    @staticmethod
    def SELECTED_STICKER_ID(sticker_id):
        return f'â¨ é¸æè²¼å ID: {sticker_id}'

    @staticmethod
    def SELECTED_STICKER(title):
        return f'â¨ é¸æè²¼å: {title}'

    @staticmethod
    def PROGRESSBAR(pb):
        return f'ð  {pb}'