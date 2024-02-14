import unittest
from Source.Models.organization import organization_model
from Source.settings import settings

class OrganizationModelTest(unittest.TestCase):
    def test_organization_model(self):
        name = "Organization"
        inn = "123456789012"
        bik = "123456789"
        account = "12345678901"
        ownership_type = "Type"

        # Создаем экземпляр настроек и передаем его в модель организации
        settings = settings()
        settings.some_setting = "some value"
        organization = organization_model(name)
        organization.set_settings(settings)

        # Проверяем, что настройки были правильно загружены
        self.assertEqual(organization.get_settings().some_setting, "some value")

        # Проверяем, что значения свойств были правильно инициализированы
        self.assertEqual(organization.name, name)
        self.assertEqual(organization.inn, inn)
        self.assertEqual(organization.bik, bik)
        self.assertEqual(organization.account, account)
        self.assertEqual(organization.ownership_type, ownership_type)

        # Проверяем, что при передаче некорректных значений свойств генерируются исключения
        with self.assertRaises(argument_exception):
            organization.inn = "123"

        with self.assertRaises(argument_exception):
            organization.bik = "1234"

        with self.assertRaises(argument_exception):
            organization.account = "1234567890123"

        with self.assertRaises(argument_exception):
            organization.ownership_type = "ABCDE"

if __name__ == "__main__":
    unittest.main()
