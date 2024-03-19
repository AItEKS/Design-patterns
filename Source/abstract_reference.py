import uuid
from abc import ABC
from Source.errors import error_proxy
from Source.exceptions import exception_proxy, argument_exception


class abstract_reference(ABC):
    _id = None
    _name = ""
    _description = ""
    _error = error_proxy()

    def __init__(self, name):
        self._id = uuid.uuid4()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        exception_proxy.validate(value.strip(), str, 50)
        self._name = value.strip()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        exception_proxy.validate(value.strip(), str)
        self._description = value.strip()

    @property
    def id(self):
        return str(self._id.hex)

    @property
    def is_error(self):
        return self._error.error != ""

    @staticmethod
    def create_dictionary(items: list):
        exception_proxy.validate(items, list)

        result = {}
        for position in items:
            result[position.name] = position

        return result

    @staticmethod
    def create_fields(source) -> list:
        if source is None:
            raise argument_exception("Некорректно переданы параметры!")

        items = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_"), dir(source)))
        result = []

        for item in items:
            attribute = getattr(source.__class__, item)
            if isinstance(attribute, property):
                result.append(item)

        return result

    def __str__(self) -> str:
        return self.id

    def __hash__(self) -> int:
        return hash(self.id)
