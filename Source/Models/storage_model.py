class srorage_model:
    def __init__(self):
        self.__address = None

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        self.__address = value
