from Source.settings_manager import settings_manager
import unittest


class settings_test(unittest.TestCase):
    def test_create_app_settings(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        result = manager.data

        # Проверки
        print(manager.data)
        print(type(manager.data))
        assert result is not None
        assert len(manager.settings.inn) > 0
        assert manager.settings.name != ""

    def test_fail_open_settings(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        manager.open("test.json")

        # Проверки
        assert manager.error.is_empty == False








