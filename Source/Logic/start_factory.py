from Source.Models.group import group_model
from Source.Models.unit import unit_model
from Source.Models.nomenclature import nomenclature_model
from Source.abstract_reference import abstract_reference
from Source.Models.receipe import receipe_model
from Source.Models.receipe_row import receipe_row_model

from Source.settings import settings
from Source.Storage.storage import storage
from Source.exceptions import exception_proxy, operation_exception, argument_exception


class start_factory:
    __options: settings = None
    __storage: storage = None

    def __init__(self, __options: settings, __storage: storage = None) -> None:
        exception_proxy.validate(__options, settings)
        self.__options = __options
        self.__storage = __storage

    def __save(self, key: str, items: list):
        exception_proxy.validate(key, str)
        if self.__storage is None:
            self.__storage = storage()

        self.__storage.data[key] = items

    @property
    def storage(self):
        return self.__storage

    @staticmethod
    def create_units():
        items = []
        items.append(unit_model.create_unit_gramm())
        items.append(unit_model.create_unit_kilogram())
        items.append(unit_model.create_unit_litr())
        items.append(unit_model.create_unit_millilitr())
        items.append(unit_model.create_unit_shtuki())

        return items

    @staticmethod
    def create_nomenclatures():
        group = group_model.create_default_group()
        items = [{"Мука пшеничная": "киллограмм"},
                 {"Сахар": "киллограмм"},
                 {"Сливочное масло": "киллограмм"},
                 {"Яйца": "штука"},
                 {"Ванилин": "грамм"},
                 {"Куриное филе": "киллограмм"},
                 {"Салат Романо": "грамм"},
                 {"Сыр Пармезан": "киллограмм"},
                 {"Чеснок": "киллограмм"},
                 {"Белый хлеб": "киллограмм"},
                 {"Соль": "киллограмм"},
                 {"Черный перец": "грамм"},
                 {"Оливковое масло": "литр"},
                 {"Лимонный сок": "литр"},
                 {"Горчица дижонская": "грамм"},
                 {"Сахарная пудра": "грамм"},
                 {"Ванилиин": "грамм"},
                 {"Корица": "грамм"},
                 {"Какао": "киллограмм"}]

        units = abstract_reference.create_dictionary(start_factory.create_units())

        result = []
        for position in items:
            _list = list(position.items())
            if len(_list) < 1:
                raise operation_exception(
                    "Невозможно сформировать элементы номенклатуры! Некорректный список исходных элементов!")

            tuple = list(_list)[0]

            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент номенклатуры. Длина кортежа не корректна!")

            name = tuple[0]
            unit_name = tuple[1]

            if not unit_name in units.keys():
                raise operation_exception(f"Невозможно найти в списке указанную единицу измерения {unit_name}!")

            item = nomenclature_model(name, group, units[unit_name])
            result.append(item)

        return result

    @staticmethod
    def create_groups():
        items = []
        items.append(group_model.create_default_group())
        return items

    @staticmethod
    def create_receipts(__data: list = None):
        result = []

        if __data is None:
            data = start_factory.create_nomenclatures()
        else:
            data = __data

        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры! Список номенклатуры пуст.")

        items = [{"Мука пшеничная": 100},
                 {"Сахар": 80},
                 {"Сливочное масло": 70},
                 {"Яйца": 1},
                 {"Ванилин": 5}]
        item = receipe_model.create_receipt("Вафли хрустящие в вафельнице", "", items, data)

        item.instructions.extend([
            "Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.",
            "Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.",
            "Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности.",
            "Всыпьте муку, добавьте ванилин.",
            "Перемешайте массу венчиком до состояния гладкого однородного теста."])

        item.comments = "Время приготовления: 20 мин. 8 порций"
        result.append(item)

        items = [{"Куриное филе": 200},
                 {"Салат Романо": 50},
                 {"Сыр Пармезан": 50},
                 {"Чеснок": 10},
                 {"Белый хлеб": 30},
                 {"Соль": 5},
                 {"Черный перец": 2},
                 {"Оливковое масло": 10},
                 {"Лимонный сок": 5},
                 {"Горчица дижонская": 5},
                 {"Яйца": 2}]
        item = receipe_model.create_receipt("Цезарь с курицей", "", items, data)

        item.instructions.extend([
            "Нарезать куриное филе кубиками, нарубите чеснок, нарежьте хлеб на кубики."
            "Очистить салат и обсушить его."
            "Натереть сыр Пармезан на терке."
            "Обжарить на сковороде куриное филе с чесноком до готовности."
            "На той же сковородке обжарьить кубики хлеба до золотистости."
            "В миске смешайте оливковое масло, лимонный сок, горчицу, измельченный чеснок, соль и перец."
            "В большой миске смешайте кубики курицы, хлеба, листья салата."
            "Добавить заправку и тщательно перемешать"])
        result.append(item)

        items = [{"Яйца": 3},
                 {"Сахарная пудра": 180},
                 {"Ванилиин": 5},
                 {"Корица": 5},
                 {"Какао": 20}]
        result.append(receipe_model.create_receipt("Безе", "", items, data))

        return result

    def create(self) -> bool:
        if self.__options.is_first_start:
            self.__options.is_first_start = False

            items = start_factory.create_nomenclatures()
            self.__save(storage.nomenclature_key(), items)

            items = start_factory.create_receipts(items)
            self.__save(storage.receipt_key(), items)

            items = start_factory.create_units()
            self.__save(storage.unit_key(), items)

            items = start_factory.create_groups()
            self.__save(storage.group_key(), items)
            return True

        else:
            return False
