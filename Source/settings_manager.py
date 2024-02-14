import os
import json
import uuid
from Source.settings import settings
from operation_exception import operation_exception
from argument_exception import argument_exception


class settings_manager(object):
    # Уникальный номер
    __unique_number = None
    # Словарь с данными
    __data = {}
    # Настройки инстанс
    __settings = settings()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def convert(self):
        if len(self.__data) == 0:
            raise operation_exception("Невозможно создать объект типа settings.py")

        fields = dir(self.__settings.__class__)
        for field in fields:
            if not field.startswith("__"):
                if field in self.__data:
                    value = self.__data[field]
                    setattr(self.__settings, field, value)

        print(self.__settings.name)

    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()

    def open(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise argument_exception("ERROR: Неверный аргумент!")

        if file_name == "":
            raise argument_exception("ERROR: Неверный аргумент!")

        self.__file_name = file_name.strip()

        try:
            self.__open()
            self.convert()
        except:
            return False

        return True

    @property
    def data(self) -> {}:
        """
            Текущие данные
        Returns:
            _type_: словарь
        """
        return self.__data

    @property
    def number(self) -> str:
        return str(self.__unique_number.hex)

    def __open(self):
        """
            Открыть файл с настройками
        Raises:
            Exception: Ошибка при открытии файла
        """
        # Проверяем, существует ли заданный файл
        if not os.path.exists(self.__file_name):
            raise operation_exception(f"ERROR: Файл {self.__file_name} не существует!")

        # Открываем файл и загружаем данные
        with open(self.__file_name, "r") as read_file:
            self.__data = json.load(read_file)