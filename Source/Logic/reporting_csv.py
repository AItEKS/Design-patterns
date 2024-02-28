from typing import Dict, List

from Source.Logic.reporting import reporting
from Source.settings import settings
from Source.Storage.storage import storage
from io import StringIO


class reporting_csv(reporting):
    def __init__(self):
        self.settings = settings()
        self.storage = storage()

    def create(self, key: str) -> str:
        if key in [self.storage.nomenclature_key(), self.storage.group_key(), self.storage.unit_key()]:
            models = self.storage.data.get(key, [])
            fields = self.get_classes_fields(models)

            csv_string = self.generate_csv_string(models, fields[key.split('_')[1]])
            return csv_string
        else:
            raise ValueError("Invalid key provided")

    def generate_csv_string(self, models: List, model_fields: List) -> str:
        if not models:
            return ""

        output = StringIO()
        headers = ";".join(model_fields) + "\n"
        output.write(headers)

        for model in models:
            values = []
            for field in model_fields:
                attribute = "_".join((model.__class__.__name__, field)).replace("-", "_").capitalize()
                try:
                    value = getattr(model, attribute)
                    values.append(str(value or ""))
                except AttributeError:
                    continue
            row_values = ";".join(values) + "\n"
            output.write(row_values)

        csv_string = output.getvalue()
        output.close()

        return csv_string