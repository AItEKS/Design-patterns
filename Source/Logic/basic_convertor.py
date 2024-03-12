from Source.Logic.convertor import convertor


class basic_convertor(convertor):

    def serialize(self, field: str, object) -> dict:
        super().serialize(field, object)

        if not isinstance(object, (int, str, bool)):
            self.error = f"Некорректный тип данных передан для конвертации. Ожидается: (int, str, bool). Передан: {type(object)}"
            return None

        try:
            return {field: object}
        except Exception as ex:
            self.set_error(ex)

        return None
