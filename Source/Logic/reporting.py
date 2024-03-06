from abc import ABC
from Source.exceptions import exception_proxy, operation_exception


class reporting(ABC):
    __data = {}
    __fields = []

    def __init__(self, _data):
        exception_proxy.validate(_data, dict)
        self.__data = _data

    def create(self, typeKey: str):
        exception_proxy.validate(typeKey, str)
        self.__fields = self.build(typeKey, self.__data)

        return ""

    @staticmethod
    def build(typeKey: str, data: dict) -> list:
        exception_proxy.validate(typeKey, str)
        if data is None:
            raise operation_exception("Набор данных не определен!")

        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")

        item = data[typeKey][0]
        result = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_"), dir(item)))

        return result

    def __build(self, typeKey: str) -> list:
        return reporting.build(typeKey, self.__data)

    @property
    def fields(self) -> list:
        return self.__fields

    @property
    def data(self) -> dict:
        return self.__data
