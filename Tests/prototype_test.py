import unittest
from Source.Logic.storage_prototype import storage_prototype
from Source.Logic.start_factory import start_factory
from Source.settings_manager import settings_manager
from Source.Storage.storage import storage
from Source.Models.nomenclature import nomenclature_model
from datetime import datetime


class prototype_test(unittest.TestCase):
    def test_filter(self):
        # Тест фильтрации данных по периоду

        # Подготовка данных для теста
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[key]

        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        prototype = storage_prototype(data)

        # Действие
        result1 = prototype.filter(start_date, stop_date)
        stop_date = datetime.strptime("2024-01-05", "%Y-%m-%d")
        result2 = result1.filter(start_date, stop_date)

        # Проверка
        self.assertIsInstance(result1, storage_prototype)
        self.assertTrue(prototype.is_empty)

    def test_filter_nom(self):
        # Тест фильтрации данных по номенклатуре

        # Подготовка данных для теста
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        nomenclatures = start.create_nomenclatures()
        nomenclature_id = nomenclatures[0].id

        # Действие
        prototype = storage_prototype(start.storage.data)
        result = prototype.filter_nom(nomenclature_id)

        # Проверка
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, nomenclature_model) for item in result))

    def test_filter_receipt(self):
        # Тест фильтрации данных по номеру накладной

        # Подготовка данных для теста
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = list(start.storage.data.values())

        receipt_id = "TestReceiptID"
        prototype = storage_prototype(data)

        # Действие
        result = prototype.filter_receipt(receipt_id)

        # Проверка
        self.assertIsInstance(result, list)
