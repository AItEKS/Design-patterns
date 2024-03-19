import os
import json
import uuid

from Source.settings import settings
from Source.errors import error_proxy
from Source.exceptions import exception_proxy


class settings_manager(object):
    _settings_file_name = "settings.json"
    _data = None
    _uniqueNumber = None
    _settings = None
    _error = error_proxy()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self._uniqueNumber is None:
            self._uniqueNumber = uuid.uuid4()
            self.open(self._settings_file_name)
            self._settings = settings()
            self.__load()

    def __open(self):
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self._settings_file_name)
        if not os.path.exists(settings_file):
            self._error.set_error(Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file))

        try:
            with open(settings_file, "r") as read_file:
                self._data = json.load(read_file)
        except:
            self._error.set_error(Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file))

    def open(self, file_name: str):
        exception_proxy.validate(file_name, str)

        self._settings_file_name = file_name
        self.__open()
        self.__load()

    def __load(self):
        if len(self._data) == 0:
            return

        fields = list(filter(lambda x: not x.startswith("_"), dir(self._settings.__class__)))

        for field in fields:
            keys = list(filter(lambda x: x == field, self._data.keys()))
            if len(keys) != 0:
                value = self._data[field]

                if not isinstance(value, list) and not isinstance(value, dict):
                    setattr(self._settings, field, value)

    @property
    def settings(self) -> settings:
        return self._settings

    @property
    def data(self):
        return self._data

    @property
    def error(self) -> error_proxy:

        return self._error
