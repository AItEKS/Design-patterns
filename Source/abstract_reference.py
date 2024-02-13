import uuid
from abc import ABC
from error_proxy import error_proxy

class abstract_reference(ABC):
    __id: uuid.UUID
    __name: str = ""
    __error: error_proxy = error_proxy()

    def __init__(self, name: str = None) -> None:
        self.name = name
        self.__id = uuid.uuid4()

    @property
    def error(self):
        """
           Работа с ошибками

        Returns:
            _type_: _description_
        """
        return self.__error

    @property
    def id(self):
        """
            Уникальный код
        Returns:
            _type_: _description_
        """
        return self.__id

    @property
    def name(self):
        """
           Наименование
        Returns:
            _type_: _description_
        """
        return self.__name.strip()

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise Exception("Неверный аргумент!")

        if len(value.strip()) > 50:
            raise Exception("Превышена максимальная длина наименования!")

        if value == "":
            raise Exception("Некорректное значение наименование!")

        self.__name = value.strip()