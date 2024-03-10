import abc
from Source.exceptions import exception_proxy
from Source.errors import error_proxy


class convertor(error_proxy):
    @abc.abstractmethod
    def convert(self, field: str, object) -> dict:
        exception_proxy.validate(field, str)
        self.clear()
