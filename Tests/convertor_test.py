import datetime
import unittest
from Source.Logic.convert_factory import convert_factory
from Source.Models.unit import unit_model


class convert_factory_test(unittest.TestCase):
    def setUp(self):
        # Подготовка
        self.factory = convert_factory()

    def test_convert_object_int(self):
        # Действие
        result = self.factory.convert_object(10)
        expected_result = {'value': 10}
        # Проверки
        self.assertEqual(str(result), str(expected_result))

    def test_convert_object_float(self):
        # Действие
        result = self.factory.convert_object(3.14)
        expected_result = {'value': 3.14}
        # Проверки
        self.assertEqual(result, expected_result)

    def test_convert_object_str(self):
        # Действие
        result = self.factory.convert_object("Hello")
        expected_result = {'value': 'Hello'}
        # Проверки
        self.assertEqual(str(result), str(expected_result))

    def test_convert_object_datetime(self):
        # Подготовка
        dt = datetime.datetime(2024, 3, 7)

        # Действие
        result = self.factory.convert_object(dt)
        expected_result = {'datetime_value': '2024-03-07 00:00:00'}

        # Проверки
        self.assertEqual(result, expected_result)

    def test_convert_object_nomenclature(self):
        nomenclature = {"name": "Product A", "price": 10}
        result = self.factory.convert_object(nomenclature)
        expected_result = {"name": {"value": "Product A"}, "price": {"value": 10}}
        self.assertEqual(result, expected_result)

    def test_convert_object_unit_model(self):
        base_unit = unit_model.create_unit_gramm()
        unit = unit_model('килограмм', base_unit, 1000)

        # Действие
        result = self.factory.convert_object(unit)

        expected_result = {
            "name": {"value": "килограмм"},
            "base_unit": {
                "name": "грамм",
                "coefficient": 1
            },
            "coefficient": 1000
        }

        if 'reference_id' in result:
            del result['reference_id']

        # Проверки
        self.assertDictEqual(result, expected_result)

    def test_convert_object_nomenclature_group(self):
        group = {"name": "Group A", "description": "Description of Group A"}

        # Действие
        result = self.factory.convert_object(group)

        expected_result = {"name": {"value": "Group A"}, "description": {"value": "Description of Group A"}}

        # Проверки
        self.assertEqual(result, expected_result)
