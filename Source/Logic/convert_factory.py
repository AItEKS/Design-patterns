import datetime
from Source.Logic.basic_convertor import basic_convertor
from Source.Logic.datetime_convertor import datetime_convertor
from Source.Logic.reference_convertor import reference_convertor
from Source.exceptions import argument_exception
from Source.Models.unit import unit_model


class convert_factory:
    def __init__(self):
        self.converters = {
            int: basic_convertor(),
            float: basic_convertor(),
            str: basic_convertor(),
            datetime.datetime: datetime_convertor(),
            dict: reference_convertor(),
            unit_model: reference_convertor()
        }

    def convert_object(self, obj):
        if type(obj) in self.converters:
            converter = self.converters[type(obj)]
            return converter.convert(obj)
        elif isinstance(obj, dict):
            converted_dict = {}
            for key, value in obj.items():
                converted_dict[key] = self.convert_object(value)
            return converted_dict
        elif isinstance(obj, unit_model):
            converter = self.converters[unit_model]
            return converter.convert(obj)
        else:
            raise argument_exception("Ошибка типа данных!")

