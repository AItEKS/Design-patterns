import json


class error_proxy:
    __error_text = ""

    def __init__(self, exception: Exception = None):
        if exception is not None:
            self.set_error(exception)

    @property
    def error(self):
        return self.__error_text

    @error.setter
    def error(self, value: str):
        if value == "":
            raise Exception("Некорректно переданы параметры!")

        self.__error_text = value

    @classmethod
    def set_error(self, exception: Exception):
        if exception is None:
            self.__error_text = ""
            return

        self.__error_text = "Ошибка! " + str(exception)

    @property
    def is_empty(self) -> bool:
        if len(self.__error_text) != 0:
            return False
        else:
            return True

    @staticmethod
    def create_error_response(app, message: str, http_code: int = 0):
        if app is None:
            raise Exception("Некорректно переданы параметры!")

        if http_code == 0:
            code = 500
        else:
            code = http_code

        json_text = json.dumps({"details": message}, sort_keys=True, indent=4, ensure_ascii=False)

        result = app.response_class(
            response=f"{json_text}",
            status=code,
            mimetype="application/json; charset=utf-8"
        )

        return result