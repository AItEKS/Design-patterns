from Source.Logic.convertor import convertor


class basic_convertor(convertor):

    def convert(self, field: str, object) -> dict:
        super().convert(field, object)

        if not isinstance(object, (int, str, bool)):
            self.error = f"Некорректный тип данных передан для конвертации: {type(object)}"
            return None
        try:
            return {field: object}
        except Exception as ex:
            self.error.set_error(ex)
        return None