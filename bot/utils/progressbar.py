class Progressbar():

    __WHITE_BLOCK = '░'
    __BLACK_BLOCK = '█'
    __LOADINGBAR_LENGTH = 10

    def __init__(self, length, display_percent=False):
        self.length = length
        self.display_percent = display_percent

    def __percent(self, current):
        return '{:.2f}%'.format(float(current * 100 / self.length))
        pass

    def circular():
        pass

    def linear():
        pass

    def loading(self, current: int) -> str:
        index = current % self.__class__.__LOADINGBAR_LENGTH
        LEFT_WHITE_BLOCK = self.__class__.__WHITE_BLOCK * index
        RIGHT_WHITE_BLOCK = self.__class__.__WHITE_BLOCK * (self.__class__.__LOADINGBAR_LENGTH - index - 1)
        MIDDLE_BLACK_BLOCK = self.__class__.__BLACK_BLOCK
        ret = LEFT_WHITE_BLOCK + MIDDLE_BLACK_BLOCK + RIGHT_WHITE_BLOCK

        if self.display_percent:
            ret += f' {self.__percent(current)}'

        return ret
