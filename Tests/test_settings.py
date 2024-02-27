from Source.settings_manager import settings_manager
import unittest


# Набор автотестов для проверки работы модуля настроек
class settings_test(unittest.TestCase):
    # Проверить на корректность создания и загрузки файла с настройками
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

    # Проверить работу менеджера загрузки настроек при не корректном файле настроек
    def test_fail_open_settings(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        manager.open("test.json")

        # Проверки
        assert manager.error.is_empty == False








