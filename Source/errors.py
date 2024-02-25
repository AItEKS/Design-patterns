class error_proxy:
    " Текст с описание ошибки "
    __error_text = ""

    def __init__(self, exception: Exception = None):
        if exception is not None:
            self.set_error(exception)

    @property
    def error(self):
        """
            Получить текстовое описание ошибки
        Returns:
            str: _description_
        """
        return self.__error_text

    @error.setter
    def error(self, value: str):
        if value == "":
            raise Exception("Некорректно переданы параметры!")

        self.__error_text = value

    @classmethod
    def set_error(self, exception: Exception):
        """
            Сохранить текстовое описание ошибки из исключения
        Args:
            exception (Exception): входящее исключение
        """

        if exception is None:
            self.__error_text = ""
            return

        self.__error_text = "Ошибка! " + str(exception)

    @property
    def is_empty(self) -> bool:
        """
            Флаг. Есть ошибка
        Returns:
            bool: _description_
        """
        if len(self.__error_text) != 0:
            return False
        else:
            return True