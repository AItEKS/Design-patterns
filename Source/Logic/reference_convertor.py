from Source.Logic.convertor import convertor
from Source.exceptions import argument_exception
from Source.Models.unit import unit_model


class reference_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, dict):
            converted_dict = {}
            for key, value in obj.items():
                converted_dict[key] = {"value": value}
            return converted_dict
        elif isinstance(obj, unit_model):
            return {
                "name": {"value": obj.name},
                "base_unit": {
                    "name": obj.base_unit.name,
                    "coefficient": obj.base_unit.coefficient
                },
                "coefficient": obj.coefficient
            }
        else:
            raise argument_exception("Ошибка типа данных!")
