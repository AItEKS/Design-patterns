import datetime
from Source.Logic.basic_convertor import basic_convertor
from Source.Logic.datetime_convertor import datetime_convertor
from Source.Logic.reference_convertor import reference_convertor
from Source.exceptions import argument_exception


class convert_factory:
    def __init__(self):
        self.converters = {
            int: basic_convertor(),
            float: basic_convertor(),
            str: basic_convertor(),
            datetime.datetime: datetime_convertor(),
            dict: reference_convertor()
        }

    def convert_object(self, obj):
        obj_type = type(obj)
        if obj_type in self.converters:
            converter = self.converters[obj_type]
            return converter.convert(obj)
        elif obj_type == dict:
            converted_dict = {}
            for key, value in obj.items():
                converted_dict[key] = self.convert_object(value)
            return converted_dict
        else:
            raise argument_exception("Ошибка типа данных!")
