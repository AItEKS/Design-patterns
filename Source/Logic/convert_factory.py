import datetime
from reference_convertor import reference_convertor
from basic_convertor import basic_convertor
from datetime_convertor import datetime_convertor
from Source.abstract_reference import abstract_reference


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
            raise ValueError("Unsupported data type for conversion")