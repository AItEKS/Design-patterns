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
                 {"Корица": "грамм"},
                 {"Какао": "киллограмм"},
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
                 {"Ванилиин": "грамм"}]

        units = abstract_reference.create_dictionary(start_factory.create_units())

        result = []
        for position in items:
            __list = list(position.items())
            if len(__list) < 1:
                raise operation_exception(
                    "Невозможно сформировать элементы номенклатуры! Некорректный список исходных элементов!")

            tuple = list(__list)[0]

            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент номенклатуры. Длина кортежа не корректна!")

            name = tuple[0]
            unit_name = tuple[1]

            item = nomenclature_model(name, group, units[unit_name])
            result.append(item)

        return result

    @staticmethod
    def create_groups():
        items = []
        items.append(group_model.create_default_group())
        return items

    @staticmethod
    def create_receipts():
        result = []
        data = start_factory.create_nomenclatures()

        # Вафли хрустящие в вафельнице
        items = [{"Мука пшеничная": 100},
                 {"Сахар": 80},
                 {"Сливочное масло": 70},
                 {"Яйца": 1},
                 {"Ванилин": 5}]
        result.append(receipe_model.create_receipt("Вафли хрустящие в вафельнице", "", items, data))

        # Цезарь с курицей
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
        result.append(receipe_model.create_receipt("Цезарь с курицей", "", items, data))

        # Безе
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

            items = start_factory.create_units()
            self.__save(storage.unit_key(), items)

            items = start_factory.create_groups()
            self.__save(storage.group_key(), items)

            items = start_factory.create_receipts()
            self.__save(storage.receipt_key(), items)

        else:
            return True
