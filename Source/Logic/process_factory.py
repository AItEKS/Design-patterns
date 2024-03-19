from Source.Logic.processing import processing
from Source.Logic.turn_processing import turn_processing
from Source.Models.storage_row_model import storage_row_model
from Source.exceptions import exception_proxy, argument_exception, operation_exception


class process_factory:
    __maps = {}

    def __init__(self) -> None:
        self.__build_structure()

    def __build_structure(self):
        self.__maps[process_factory.turn_key()] = turn_processing

    def create(self, process_key: str) -> processing:
        exception_proxy.validate(process_key, str)
        if process_key not in self.__maps.keys():
            raise argument_exception(f"Указанный процесс {process_key} не реализован!")

        current_processing = self.__maps[process_key]
        if current_processing is None:
            raise operation_exception("Некорректно сконфигурирована текущая фабрика!")

        return current_processing

    @staticmethod
    def turn_key() -> str:
        return "turns"

    @staticmethod
    def process_keys(cls):
        keys = []
        methods = [getattr(cls, method) for method in dir(cls) if callable(getattr(cls, method))]
        for method in methods:
            if method.__name__.endswith("_key") and callable(method):
                keys.append(method())
        return keys