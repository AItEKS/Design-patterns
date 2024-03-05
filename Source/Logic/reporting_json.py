import json
from typing import Dict, List

from Source.Logic.reporting import reporting
from Source.settings import settings
from Source.Storage.storage import storage
from io import StringIO


class reporting_json(reporting):
    def __init__(self):
        self.settings = settings()
        self.storage = storage()

    def create(self, key: str) -> str:
        if key in [self.storage.nomenclature_key(), self.storage.group_key(), self.storage.unit_key()]:
            models = self.storage.data.get(key, [])
            fields = self.get_classes_fields(models)

            json_string = self.generate_json_string(models, fields[key.split('_')[1]])
            return json_string
        else:
            raise ValueError("Invalid key provided")

    def generate_json_string(self, models: List, model_fields: List) -> str:
        if not models:
            return ""

        output = StringIO()
        output.write('[')

        for model in models:
            json_object = {}
            for field in model_fields:
                attribute = "_".join((model.__class__.__name__, field)).replace("-", "_").capitalize()
                try:
                    value = getattr(model, attribute)
                    json_object[field] = value
                except AttributeError:
                    continue
            json_string = json.dumps(json_object, ensure_ascii=False)
            output.write(json_string + ',')

        output.write(']')

        json_string = output.getvalue()
        output.close()

        return json_string