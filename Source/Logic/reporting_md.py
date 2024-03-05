import json
from typing import Dict, List

from Source.Logic.reporting import reporting
from Source.settings import settings
from Source.Storage.storage import storage
from io import StringIO


class reporting_md(reporting):
    def __init__(self):
        self.settings = settings()
        self.storage = storage()

    def create(self, key: str) -> str:
        if key in [self.storage.nomenclature_key(), self.storage.group_key(), self.storage.unit_key()]:
            models = self.storage.data.get(key, [])
            fields = self.get_classes_fields(models)

            md_string = self.generate_md_string(models, fields[key.split('_')[1]])
            return md_string
        else:
            raise ValueError("Invalid key provided")

    def generate_md_string(self, models: List, model_fields: List) -> str:
        if not models:
            return ""

        output = StringIO()
        output.write('|')

        for field in model_fields:
            output.write('|' + field + '|')

        output.write('|\n')

        for model in models:
            output.write('|')

            for field in model_fields:
                attribute = "_".join((model.__class__.__name__, field)).replace("-", "_").capitalize()
                try:
                    value = getattr(model, attribute)
                    output.write('|' + str(value) + '|')
                except AttributeError:
                    output.write('|' + '-' + '|')

            output.write('|\n')

        md_string = output.getvalue()
        output.close()

        return md_string