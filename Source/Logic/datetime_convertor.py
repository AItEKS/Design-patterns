import datetime
from convertor import convertor


class datetime_convertor(convertor):
    def convert(self, obj):
        if isinstance(obj, datetime.datetime):
            return {"datetime_value": obj.strftime("%Y-%m-%d %H:%M:%S")}
        else:
            raise ValueError("Unsupported data type for datetime conversion")

