from Source.errors import error_proxy
from datetime import datetime
from Source.Models.nomenclature import nomenclature_model


class storage_prototype(error_proxy):
    __data = []

    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            self.error = "Некорректно переданы параметры!"

        self.__data = data

    def filter(self, start_period: datetime, stop_period: datetime):
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if start_period > stop_period:
            self.error = "Некорректный период!"

        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)

        return storage_prototype(result)

    def filter_nom(self, nomenclature_id: str):
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.nomenclature_id == nomenclature_id:
                result.append(item)

        return storage_prototype(result)

    def filter_receipt(self, receipt_row: str):
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"

        if not self.is_empty:
            return self.__data

        result = []
        for item in self.__data:
            if item.receipt_row == receipt_row:
                result.append(item)

        return storage_prototype(result)

    @property
    def data(self):
        return self.__data