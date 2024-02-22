from Source.Models.unit import unit_model
from Source.Logic.start_factory import start_factory
from Source.settings_manager import settings_manager
from Source.Storage.storage import storage
from Source.Models.storage import storage_model

import unittest


#
# Набор автотестов для проверки работы фабричного метода
# #
class factory_test(unittest.TestCase):
    #
    # Проверка создания ед. измерения
    #
    def test_check_factory(self):
        # Подготовка
        unit = unit_model.create_unit_kilogram()

        # Действие

        # Проверки
        assert unit is not None

    #
    # Проверка создание начальной номенклатуры
    #
    def test_check_create_nomenclature(self):
        # Подготовка
        items = start_factory.create_nomenclature()

        # действие

        # Прверки
        assert len(items) > 0


    def test_recipe_ingredients(self):
        recipe = storage_model('Тестовый рецепт')
        recipe.add_ingredient('Мука', 100, 'грамм')
        recipe.add_ingredient('Сахар', 80, 'грамм')
        recipe.add_ingredient('Сливочное масло', 70, 'грамм')
        recipe.add_ingredient('Яйцо куриное', 1, 'штука')
        # print(recipe.ingredients)
        # Проверяем, что все добавленные ингредиенты есть в рецепте
        ingredients_list = list(recipe.ingredients.keys())

        self.assertIn('Мука', ingredients_list)
        self.assertIn('Сахар', ingredients_list)
        self.assertIn('Сливочное масло', ingredients_list)
        self.assertIn('Яйцо куриное', ingredients_list)

    def setUp(self):
        self.unit_gramm = unit_model.create_unit_gramm()
        self.unit_kilogram = unit_model.create_unit_kilogram()
        self.unit_millilitr = unit_model.create_unit_millilitr()
        self.unit_litr = unit_model.create_unit_litr()
        self.unit_shtuki = unit_model.create_unit_shtuki()

    def test_base_unit(self):
        self.assertIsNone(self.unit_gramm.base_unit, "Base unit for gram is not initialized")
        self.assertIsNotNone(self.unit_kilogram.base_unit, "Base unit for kilogram is not initialized")
        self.assertIsNone(self.unit_millilitr.base_unit, "Base unit for milliliter is not initialized")
        self.assertIsNotNone(self.unit_litr.base_unit, "Base unit for liter is not initialized")
        self.assertIsNone(self.unit_shtuki.base_unit, "Base unit for piece is not initialized")

    def test_coefficient(self):
        self.assertEqual(self.unit_gramm.coefficient, 1, "Incorrect coefficient for gram")
        self.assertEqual(self.unit_kilogram.coefficient, 1000, "Incorrect coefficient for kilogram")
        self.assertEqual(self.unit_millilitr.coefficient, 1, "Incorrect coefficient for milliliter")
        self.assertEqual(self.unit_litr.coefficient, 1000, "Incorrect coefficient for liter")
        self.assertEqual(self.unit_shtuki.coefficient, 1, "Incorrect coefficient for piece")