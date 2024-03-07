from Source.Logic.convertor import convertor
from Source.exceptions import argument_exception


class basic_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, (int, float, str)):
            return {"value": obj}
        else:
            raise argument_exception("Ошибка типа данных!")
