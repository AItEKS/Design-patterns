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
        print(recipe.ingredients)
        # Проверяем, что все добавленные ингредиенты есть в рецепте
        ingredients_list = list(recipe.ingredients.keys())

        self.assertIn('Мука', ingredients_list)
        self.assertIn('Сахар', ingredients_list)
        self.assertIn('Сливочное масло', ingredients_list)
        self.assertIn('Яйцо куриное', ingredients_list)