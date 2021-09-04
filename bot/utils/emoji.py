VARIATION = '\U0000FE0F'
KEYCAP = '\U000020E3'

NEXT_PAGE = '\U000027A1'
PREVIOUS_PAGE = '\U00002B05'

def emojiNum(num: int) -> str:
    emoji_list = []
    for i in str(num):
        emoji_list.append(i + VARIATION + KEYCAP)
    return ''.join(emoji_list)
