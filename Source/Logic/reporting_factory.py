from Source.Logic.reporting import reporting
from Source.Logic.reporting_md import reporting_md
from Source.Logic.reporting_csv import reporting_csv
from Source.Logic.reporting_json import reporting_json
from Source.exceptions import exception_proxy, argument_exception, operation_exception


class report_factory:
    __maps = {}

    def __init__(self) -> None:
        self.__build_structure()

    def __build_structure(self):
        self.__maps["csv"] = reporting_csv
        self.__maps["markdown"] = reporting_md
        self.__maps["json"] = reporting_json

    def create(self, format: str, data: dict) -> reporting:
        exception_proxy.validate(format, str)
        exception_proxy.validate(data, dict)

        if len(data) == 0:
            raise argument_exception("Пустые данные")

        if format not in self.__maps.keys():
            raise operation_exception(f"Для {format} нет обработчика")

        report_type = self.__maps[format]
        result = report_type(data)
        return result

    def create_response(self, format: str, data: dict, storage_key: str, app):
        if app is None:
            raise argument_exception("Некорректно переданы параметры!")
        exception_proxy.validate(storage_key, str)

        report = self.create(format, data)
        info = report.create(storage_key)

        result = app.response_class(
            response=f"{info}",
            status=200,
            mimetype=self.mimetype
        )

        return result