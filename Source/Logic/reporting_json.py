from Source.Logic.reporting import reporting
from Source.exceptions import operation_exception
import json


class reporting_json(reporting):
    def create(self, typeKey: str):
        super().create(typeKey)
        result = []

        items = self.data[typeKey]
        if items is None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")

        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")

        data = {}
        for item in items:
            for field in self.fields:
                value = getattr(item, field)
                data[field] = value

            result.append(data)

        data = json.dumps(result)
        return data