from Source.errors import error_proxy


# Абстрактный класс для наследования
class exception_proxy(Exception):
    __error: error_proxy = error_proxy()

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.__error.set_error(self)

    @property
    def error(self):
        return self.__error

    @staticmethod
    def validate(value, type_, len_=None):
        # Проверка типа
        if not isinstance(value, type_):
            raise argument_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise argument_exception("Некорректная длина аргумента")

        return True


# Исключение при проверки аргументов
class argument_exception(exception_proxy):
    pass


# Исключение при выполнении операции
class operation_exception(argument_exception):
    pass
