from Source.errors import error_proxy


class exception_proxy(Exception):
    _error: error_proxy = error_proxy()

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self._error.set_error(self)

    @property
    def error(self):
        return self._error

    @staticmethod
    def validate(value, type_, len_=None):
        if value is None:
            raise argument_exception("Пустой аргумент")

        if not isinstance(value, type_):
            raise argument_exception("Некорректный тип")

        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise argument_exception("Некорректная длина аргумента")

        return True


class argument_exception(exception_proxy):
    pass


class operation_exception(exception_proxy):
    pass
