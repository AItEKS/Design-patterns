from Source.Logic.convertor import convertor
from Source.abstract_reference import abstract_reference
from Source.exceptions import argument_exception


class reference_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, abstract_reference):
            return {"reference_id": obj.id}
        else:
            raise argument_exception("Ошибка типа данных!")
