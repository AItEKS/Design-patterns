from Source.Models.group import group_model
from Source.Models.group_nomenclature import group_nomenclature_model
from Source.Models.unit import unit_model
from Source.exceptions import argument_exception

import unittest


class nomenclature_test(unittest.TestCase):
    def test_create_nomenclature(self):
        # Подготовка
        group = group_model("test group")
        item = group_nomenclature_model("test")
        unit = unit_model("test unit")

        # Действие
        item.description = "test description"
        item.group = group
        item.unit = unit

        # Проверка
        assert item is not None

    def test_create_nomenclature_fail_name(self):
        # Подготовка
        group = group_model("test group")
        item = group_nomenclature_model("test nomenclature")
        unit = unit_model("test unit")
        item.description = "test description"
        item.group = group
        item.unit = unit

        # Действие
        with self.assertRaises(argument_exception) as context:
            item.name = "11111111111111111111111111111111111111111111111111111111111111111111111111"
        
        # Проверка    
        self.assertTrue(f'Есть нужное исключение - {context.exception}')