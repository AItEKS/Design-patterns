from convertor import convertor
from Source.abstract_reference import abstract_reference


class reference_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, abstract_reference):
            return {"reference_id": obj.id}
        else:
            raise ValueError("Unsupported data type for reference conversion")