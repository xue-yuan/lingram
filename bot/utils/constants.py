class Message():

    START="""
    🍺 歡迎使用 @lingrambot，輸入 / 可以查看可用指令。有任何問題可以上 <a href="https://github.com/xue-yuan/lingram">GitHub</a> 跟我反應ㄛ
    """

    SEARCH_RESULT = '✨ 搜尋結果'
    DOWNLOADING = '🛠 下載中'
    DOWNLOAD_SUCCESS = '🛠 下載完畢'
    MAKING = '🛠 製作中'
    MAKE_SUCCESS = '🛠 製作完畢'
    NOT_IN_DATABASE = '💡 資料庫無貼圖資訊，製作時間約 2 分鐘'

    DOWNLOAD_FAILED = '❌ 下載失敗，請重新操作'
    MAKE_FAILED = '❌ 製作失敗，請重新操作'
    SEARCH_FAILED = '❌ 搜尋失敗，請重新操作'
    TYPE_NOT_SUPPORT = '❌ 貼圖類型目前不支援'
    UNKNOWN = "❌ Sorry, I didn't understand that command"
    MISSING_ARGS = '❌ Missing keyword(s)'

    @staticmethod
    def IS_IN_DATABASE(url):
        return f'✅ 貼圖存在於資料庫，<a href="{url}">點擊新增</a>'

    @staticmethod
    def CREATE_SUCCESS(title, url):
        return f'⚡️ 點擊新增 <a href="{url}">{title}</a>'

    @staticmethod
    def SEARCH(title):
        return f'🔎 搜尋 <b>{title}</b>'

    @staticmethod
    def SELECTED_STICKER_ID(sticker_id):
        return f'✨ 選擇貼圖 ID: {sticker_id}'

    @staticmethod
    def SELECTED_STICKER(title):
        return f'✨ 選擇貼圖: {title}'

    @staticmethod
    def PROGRESSBAR(pb):
        return f'🛠 {pb}'