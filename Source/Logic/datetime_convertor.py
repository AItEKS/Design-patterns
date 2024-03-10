import datetime
from Source.Logic.convertor import convertor
from Source.exceptions import argument_exception


class datetime_convertor(convertor):
    def convert(self, field: str,  obj):
        if isinstance(obj, datetime.datetime):
            return {"datetime_value": obj.strftime("%Y-%m-%d %H:%M:%S")}
        else:
            raise argument_exception("Ошибка типа данных!")

