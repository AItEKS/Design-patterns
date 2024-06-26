import unittest
from Source.settings_manager import settings_manager
from Source.Logics.start_factory import start_factory
from Source.exceptions import operation_exception

class storage_test(unittest.TestCase):

    #
    # Проверить сохранение данных
    #
    def test_check_save(self):
        # Подготовка
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()
        storage = start.storage

        # Действие
        result = storage.save()

        # Проверки
        assert result == True

    #
    # Проверить загрузку данных
    #    
    def test_check_load(self):
        # Подготовка
        options = settings_manager()
        start = start_factory(options.settings)
        start.create()
        storage = start.storage


        # Действие
        storage.load()

        # Проверки
        assert len(storage.data) > 0

      
