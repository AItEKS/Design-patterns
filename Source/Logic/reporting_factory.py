from typing import Dict, List

from Source.Logic.reporting_csv import reporting_csv
from Source.settings import settings
from Source.Storage.storage import storage
from Source.Logic.reporting_json import reporting_json
from Source.Logic.reporting_md import reporting_md


class reporting_factory:
    def __init__(self):
        self.settings = settings()
        self.storage = storage()

    def create(self, key: str, format: str) -> str:
        if key in [self.storage.nomenclature_key(), self.storage.group_key(), self.storage.unit_key()]:
            models = self.storage.data.get(key, [])
            fields = self.get_classes_fields(models)

            if format == "json":
                return reporting_json().create(key)
            elif format == "csv":
                return reporting_csv().create(key)
            elif format == "md":
                return reporting_md().create(key)
            else:
                raise ValueError("Invalid format provided")
        else:
            raise ValueError("Invalid key provided")

    def get_classes_fields(self, models: List) -> List:
        fields = []
        for model in models:
            for field in model.__dict__:
                if field.startswith("_"):
                    fields.append(field)
        return fields