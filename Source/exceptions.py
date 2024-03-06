from Source.errors import error_proxy


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
        if not isinstance(value, type_):
            raise argument_exception("Некорректный тип")

        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise argument_exception("Некорректная длина аргумента")

        return True


class argument_exception(exception_proxy):
    pass


class operation_exception(argument_exception):
    pass
