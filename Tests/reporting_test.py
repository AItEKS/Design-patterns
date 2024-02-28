import unittest
from Source.Logic.reporting_csv import reporting
from Source.Models.nomenclature import nomenclature_model


class test_reporting(unittest.TestCase):
    def test_generate_csv_string(self):
        report_generator = reporting()
        # Создаем тестовые данные
        test_data = [
            nomenclature_model("Test Nomenclature 1", group=None, unit=None),
            nomenclature_model("Test Nomenclature 2", group=None, unit=None)
        ]

        # Получаем поля класса nomenclature_model
        fields = report_generator.get_classes_fields([nomenclature_model])["nomenclature"]

        # Генерируем CSV строку
        csv_string = report_generator.generate_csv_string(test_data, fields)

        # Проверяем ожидаемый результат
        expected_csv = "name\nTest Nomenclature 1\nTest Nomenclature 2\n"
        self.assertEqual(csv_string, expected_csv)