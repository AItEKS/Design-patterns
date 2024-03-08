import unittest
from Source.Logic.convert_factory import convert_factory
from Source.Models.unit import unit_model
from Source.Models.nomenclature import nomenclature_model


class convert_factory_test(unittest.TestCase):
    def test_convert_object_unit_model(self):
        factory = convert_factory()
        unit = unit_model.create_unit_gramm()
        converted_unit = factory.convert_object(unit)

        self.assertEqual(converted_unit.name, 'грамм')
        self.assertEqual(converted_unit.base_unit, None)
        self.assertEqual(converted_unit.coefficient, 1)

    def test_convert_object_nomenclature_model(self):
        factory = convert_factory()
        group = unit_model.create_unit_shtuki()
        unit = unit_model.create_unit_gramm()
        nomenclature = nomenclature_model('Test Item', group, unit)
        converted_nomenclature = factory.convert_object(nomenclature)

        self.assertEqual(converted_nomenclature.name, 'Test Item')
        self.assertEqual(converted_nomenclature.group.name, 'Группа')
        self.assertEqual(converted_nomenclature.unit.name, 'грамм')