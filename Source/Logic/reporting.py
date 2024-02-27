from collections import defaultdict
from typing import Dict, List

from abc import ABC
from Source.settings import settings
from Source.Storage.storage import storage
from Source.Models.group import group_model
from Source.Models.unit import unit_model
from Source.Models.nomenclature import nomenclature_model
from io import StringIO


class reporting:
    def __init__(self):
        self.settings = settings()
        self.storage = storage()

    def get_classes_fields(self, class_list: List[type]) -> Dict[str, List]:
        classes_fields = defaultdict(list)

        for klass in class_list:
            obj = klass()
            fields = filter(lambda f: not f.startswith("__"), dir(obj.__class__))
            for field in fields:
                classes_fields[klass.__name__.lower()].append(field)

        return dict(classes_fields)

    def create(self, key: str) -> str:
        if key == self.storage.nomenclature_key():
            nomenclature_models = self.storage.data.get(self.storage.nomenclature_key(), [])
            fields = self.get_classes_fields([nomenclature_model])

            csv_string = self.generate_csv_string(nomenclature_models, fields["nomenclature"])
            return csv_string
        elif key == self.storage.group_key():
            group_models = self.storage.data.get(self.storage.group_key(), [])
            fields = self.get_classes_fields([group_model])

            csv_string = self.generate_csv_string(group_models, fields["group"])
            return csv_string
        elif key == self.storage.unit_key():
            unit_models = self.storage.data.get(self.storage.unit_key(), [])
            fields = self.get_classes_fields([unit_model])

            csv_string = self.generate_csv_string(unit_models, fields["unit"])
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