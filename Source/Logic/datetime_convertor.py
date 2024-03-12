from Source.Logic.convertor import convertor
from datetime import datetime


class datetime_convertor(convertor):
    def serialize(self, field: str, object):
        super().serialize(field, object)

        if not isinstance(object, datetime):
            self.__error.error = f"Некорректный тип данных передан для конвертации. Ожидается: datetime. Передан: {type(object)}"
            return None

        try:
            return {field: object.strftime('%YYYY-%mm-%dd %HH:%ss')}
        except Exception as ex:
            self.set_error(ex)
