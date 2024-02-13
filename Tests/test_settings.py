from Source.setting import settings
from Source.settings_manager import settings_manager
import unittest


class test_settings(unittest.TestCase):

    def test_check_create_manager(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()

        # Проверка
        print(str(manager1.number))
        print(str(manager2.number))

        assert manager1.number == manager2.number

    def test_check_name(self):
        # Подготовка
        item = settings()

        # Действие
        item.name = "a  "

        # Проверка
        assert item.name == "a"

    def test_check_manager_convert(self):
        # Подготовка
        manager = settings_manager()
        manager.open("settings.json")

        # Действие
        manager.convert()

        # Проверка    

    def test_check_open_settings(self):
        # Подготовка
        manager = settings_manager()

        # Действие
        result = manager.open("settings.json")

        # Проверка
        print(manager.data)
        assert result == True

    def test_load_settings(self):
        # Подготовка
        data = {
            "name": "Company",
            "inn": "123456789012",
            "account": "12345678901",
            "correspondent_account": "98765432109",
            "bik": "987654321",
            "ownership_type": "ABCDE"
        }

        # Действие
        item = settings()
        item.name = data["name"]
        item.inn = data["inn"]
        item.account = data["account"]
        item.correspondent_account = data["correspondent_account"]
        item.bik = data["bik"]
        item.ownership_type = data["ownership_type"]

        # Проверка
        self.assertEqual(item.name, data["name"])
        self.assertEqual(item.inn, data["inn"])
        self.assertEqual(item.account, data["account"])
        self.assertEqual(item.correspondent_account, data["correspondent_account"])
        self.assertEqual(item.bik, data["bik"])
        self.assertEqual(item.ownership_type, data["ownership_type"])


def test_check_open_settings_with_custom_path(self):
    # Подготовка
    manager = settings_manager()

    # Действие
    result = manager.open("settings.json")  # путь к файлу настроек

    # Проверка
    self.assertTrue(result)
    self.assertEqual(manager.data["name"], "Company")
    self.assertEqual(manager.data["inn"], "123456789012")
    self.assertEqual(manager.data["account"], "12345678901")
    self.assertEqual(manager.data["correspondent_account"], "98765432109")
    self.assertEqual(manager.data["bik"], "987654321")
    self.assertEqual(manager.data["ownership_type"], "ABCDE")
