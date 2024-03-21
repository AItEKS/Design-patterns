from Source.Logic.storage_prototype import storage_prototype
from Source.Logic.start_factory import start_factory
import unittest
from Source.settings_manager import settings_manager
from Source.Storage.storage import storage
from Source.Models.nomenclature import nomenclature_model
from datetime import datetime


class prototype_test(unittest.TestCase):
    def test_check_prototype(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[key]

        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        prototype = storage_prototype(data)

        # Дейтсвие
        result1 = prototype.filter(start_date, stop_date)
        stop_date = datetime.strptime("2024-01-05", "%Y-%m-%d")
        result2 = result1.filter(start_date, stop_date)

        # Проверка
        assert isinstance(result1, storage_prototype)
        assert prototype.is_empty


    def test_filter_nom(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[key]

        nomenclature = nomenclature_model("Test Nomenclature")
        prototype = storage_prototype(data)

        # Действие
        result = prototype.filter_nom(nomenclature)

        # Проверка
        assert isinstance(result, nomenclature_model)

    def test_filter_combination(self):
        # Подготовка данных для теста
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[key]

        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")

        prototype = storage_prototype(data)
        nomenclature = nomenclature_model("Test Nomenclature")

        # Действие
        result1 = prototype.filter(start_date, stop_date)
        result2 = result1.filter_nom(nomenclature)

        # Проверка
        assertIsInstance(result2, storage_prototype)


