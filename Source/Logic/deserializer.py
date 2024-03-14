import json
from Source.Models.unit import unit_model
from Source.Models.nomenclature import nomenclature_model

from Source.exceptions import argument_exception


class deserializer:
    @staticmethod
    def deserialize(json_data, model_class):
        data = json.loads(json_data)

        if model_class == unit_model:
            name = data.get('name')
            base_unit = deserializer.deserialize(data.get('base_unit'), unit_model) if data.get('base_unit') else None
            coefficent = data.get('coefficient')

            return unit_model(name, base_unit, coefficent)

        elif model_class == nomenclature_model:
            name = data.get('name')
            group = deserializer.deserialize(data.get('group'), unit_model) if data.get('group') else None
            unit = deserializer.deserialize(data.get('unit'), unit_model) if data.get('unit') else None

            return nomenclature_model(name, group, unit)

        else:
            raise argument_exception('Неподдерживаемая модель для десериализации')