from Source.Logic.reporting import reporting
from Source.exceptions import operation_exception
import json
from Source.Logic.convert_factory import convert_factory


class reporting_json(reporting):
    def create(self, typeKey: str):
        super().create(typeKey)
        result = []

        items = self.data[typeKey]
        if items is None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")

        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")

        converter = convert_factory()

        for item in items:
            converted_item = {}
            for field in self.fields:
                value = getattr(item, field)
                converted_value = converter.convert_object(value)
                converted_item[field] = converted_value

            result.append(converted_item)

        data = json.dumps(result)
        return data
