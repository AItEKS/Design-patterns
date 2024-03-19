import unittest
from Source.Logic.start_factory import start_factory
from Source.settings_manager import settings_manager
from Source.Logic.process_factory import process_factory
from Source.Storage.storage import storage
from Source.Logic.processing import processing


class processing_test(unittest.TestCase):
    def test_check_process_factory(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()

        # Действие
        result = factory.create(process_factory.turn_key())

        # Проверка
        assert result is not None

    def test_check_process_turn(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = process_factory()
        key = storage.storage_transaction_key()
        transactions = start.storage.data[key]
        processing = factory.create(process_factory.turn_key())

        # Действие
        result = processing().process(transactions)

        # Проверка
        assert result is not None
        assert len(result) > 0
        turn = list(filter(lambda x: x.nomenclature.name == "Сыр Пармезан", result))
        assert turn[0].value == 0.5
