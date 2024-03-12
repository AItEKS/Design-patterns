import unittest
from Source.Logic.reporting import reporting
from Source.Models.unit import unit_model
from Source.Storage.storage import storage
from Source.Logic.reporting_csv import reporting_csv
from Source.Models.nomenclature import nomenclature_model
from Source.Models.group import group_model
from Source.Logic.reporting_md import reporting_md
from Source.Logic.reporting_json import reporting_json


class reporting_test(unittest.TestCase):
    def test_check_json_reporting_build(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_unit_gramm()
        list.append(item)
        key = storage.unit_key()
        data[key] = list
        report = reporting_json(data)

        # Действие
        result = report.create(key)

        # Проверки
        assert result is not None
        assert len(result) > 0

    def test_check_reporting_build(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_unit_gramm()
        list.append(item)
        data[storage.unit_key()] = list

        # Дейстие
        result = reporting.build(storage.unit_key(), data)

        # Проверки
        assert result is not None
        assert len(result) > 0

    def test_check_csv_create_unit_key(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_unit_gramm()
        list.append(item)
        key = storage.unit_key()
        data[key] = list
        report = reporting_csv(data)

        # Действие
        result = report.create(key)

        # Проверки
        assert result is not None
        assert len(result) > 0

    def test_check_csv_create_nomenclature_key(self):
        # Подготовка
        data = {}
        list = []

        unit = unit_model.create_unit_kilogram()
        group = group_model.create_default_group()
        item = nomenclature_model("Тушка бройлера", group, unit)
        item.description = "Ингредиент для салата"
        list.append(item)

        key = storage.nomenclature_key()

        data[key] = list
        report = reporting_csv(data)

        # Действие
        result = report.create(key)

        # Проверки
        assert result is not None
        assert len(result) > 0

        file = open("csv_report.csv", "w")
        file.write(result)
        file.close()

    def test_check_markdown_create_unit_key(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_unit_gramm()
        list.append(item)
        key = storage.unit_key()
        data[key] = list
        report = reporting_md(data)

        # Действие
        result = report.create(key)

        # Проверки
        assert result is not None
        assert len(result) > 0

        file = open("markdown_report.md", "w")
        file.write(result)
        file.close()
