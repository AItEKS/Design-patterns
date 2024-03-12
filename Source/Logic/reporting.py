from abc import ABC, abstractmethod
from Source.exceptions import exception_proxy, operation_exception
from Source.abstract_reference import abstract_reference


class reporting(ABC):
    __data = {}
    __fields = []

    def __init__(self, _data):
        exception_proxy.validate(_data, dict)
        self.__data = _data

    @abstractmethod
    def create(self, storage_key: str):
        exception_proxy.validate(storage_key, str)
        self.__fields = self.build(storage_key, self.__data)

        return ""

    def mimetype(self) -> str:
        return "application/text"

    @staticmethod
    def build(storage_key: str, data: dict) -> list:
        exception_proxy.validate(storage_key, str)
        if data is None:
            raise operation_exception("Набор данных не определен!")

        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")

        item = data[storage_key][0]
        result = abstract_reference.create_fields(item)
        return result

    def _build(self, storage_key: str) -> list:
        return reporting.build(storage_key, self.__data)

    @property
    def fields(self) -> list:
        return self.__fields

    @property
    def data(self) -> dict:
        return self.__data
