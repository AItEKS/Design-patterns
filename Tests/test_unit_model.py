import unittest
from Source.Models.unit import unit_model
from Source.operation_exception import operation_exception
from Source.argument_exception import argument_exception


class test_unit_model(unittest.TestCase):
    def test_unit_model(self):
        # Подготовка
        name = "Length"
        base_unit = "meter"
        unit_ratio = 100

        unit = unit_model(name, base_unit, unit_ratio)

        # Проверка
        self.assertEqual(unit.name, name)
        self.assertEqual(unit.base_unit, base_unit)
        self.assertEqual(unit.unit_ratio, unit_ratio)

        with self.assertRaises(argument_exception):
            unit.base_unit = ""

        with self.assertRaises(argument_exception):
            unit.unit_ratio = ""

        with self.assertRaises(argument_exception):
            unit.base_unit = 123