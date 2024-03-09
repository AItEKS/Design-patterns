from Source.Logic.convertor import convertor


class reference_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                if isinstance(value, dict):
                    result[key] = self.convert(value)
                else:
                    result[key] = value
            return result
        else:
            return obj
