import datetime
from Source.Logic.reference_convertor import reference_convertor
from Source.Logic.basic_convertor import basic_convertor
from Source.Logic.datetime_convertor import datetime_convertor
from Source.abstract_reference import abstract_reference
from Source.exceptions import argument_exception


class convert_factory:
    def __init__(self):
        self.converters = {
            int: basic_convertor(),
            float: basic_convertor(),
            str: basic_convertor(),
            datetime.datetime: datetime_convertor(),
            abstract_reference: reference_convertor()
        }

    def convert_object(self, obj):
        if type(obj) in self.converters:
            converter = self.converters[type(obj)]
            return converter.convert(obj)
        else:
            raise argument_exception("Ошибка типа данных!")
