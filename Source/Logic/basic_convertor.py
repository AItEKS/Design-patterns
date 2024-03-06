from convertor import convertor


class basic_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, (int, float, str)):
            return {"value": obj}
        else:
            raise ValueError("Unsupported data type for basic conversion")