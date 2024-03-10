from Source.Logic.start_factory import start_factory
from Source.settings_manager import settings_manager
from Source.Storage.storage import storage

import unittest


class factory_test(unittest.TestCase):
    def test_check_create_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()

        # Действие

        # Проверки
        assert len(items) > 0

    def test_check_create_nomenclatures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()

        # Действие

        # Прверки
        assert len(items) > 0

    def test_check_create_units(self):
        # Подготовка
        items = start_factory.create_units()

        # Действие

        # Проверки
        assert len(items) > 0

    def test_check_create_groups(self):
        # Подготовка
        items = start_factory.create_groups()

        # Действие

        # Проверки
        assert len(items) > 0

    def test_check_factory_create(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory(manager.settings)

        # Действие
        result = factory.create()

        # Проверка
        if manager.settings.is_first_start:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key in factory.storage.data
            assert storage.receipt_key in factory.storage.data
            assert storage.group_key in factory.storage.data
            assert storage.unit_key in factory.storage.data
        else:
            assert result == False
