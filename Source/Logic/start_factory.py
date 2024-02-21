from Source.Models.group import group_model
from Source.Models.nomenclature import nomenclature_model
from Source.Models.unit import unit_model
from Source.settings import settings
from Source.Storage.storage import storage
from Source.exceptions import exception_proxy
from Source.Models.receipe import receipe_model
from Source.Models.storage import storage_model


class start_factory:
    __options: settings = None
    __storage: storage = None

    def __build(self):
        if self.__storage is None:
            self.__storage = storage()

        self.__storage.data[storage.nomenclature_key()] = start_factory.create_nomenclature()
        self.__storage.data[storage.group_key()] = start_factory.create_nomenclature()
        self.__storage.data[storage.unit_key()] = start_factory.create_nomenclature()

    def __init__(self, __options: settings, __storage: storage = None) -> None:
        exception_proxy.validate(__options, settings)
        self.__options = __options
        self.__storage = __storage

        self.__build()

    def __save(self, key: str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """

        exception_proxy.validate(key, str)

        if self.__storage == None:
            self.__storage = storage()

        self.__storage.data[key] = items


    @property
    def storage(self):
        """
             Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage

    @staticmethod
    def create_nomenclature():
        my_list = []

        item1 = nomenclature_model('Мука')
        item1.group = group_model.create_group('Пшеничная мука')
        item1.unit = unit_model.create_unit_kilogram()
        my_list.append(item1)

        item2 = nomenclature_model('Сахар')
        item2.group = group_model.create_group('Приправа')
        item2.unit = unit_model.create_unit_gramm()
        my_list.append(item2)

        item3 = nomenclature_model('Сливочное масло')
        item3.group = group_model.create_group('Масло')
        item3.unit = unit_model.create_unit_kilogram()
        my_list.append(item3)

        item4 = nomenclature_model('Куриное филе')
        item4.group = group_model.create_group('Мясо')
        item4.unit = unit_model.create_unit_kilogram()
        my_list.append(item4)

        item5 = nomenclature_model('Салат Романно')
        item5.group = group_model.create_group('Овощи')
        item5.unit = unit_model.create_unit_gramm()
        my_list.append(item5)

        item6 = nomenclature_model('Яйцо куриное')
        item6.group = group_model.create_group('Яйцо')
        item6.unit = unit_model.create_unit_shtuki()
        my_list.append(item6)

        item7 = nomenclature_model('Чеснок')
        item7.group = group_model.create_group('Овощи')
        item7.unit = unit_model.create_unit_gramm()
        my_list.append(item7)

        item8 = nomenclature_model('Сыр Пармезан')
        item8.group = group_model.create_group('Сыр')
        item8.unit = unit_model.create_unit_gramm()
        my_list.append(item8)

        item9 = nomenclature_model('Оливковое масло')
        item9.group = group_model.create_group('Масло')
        item9.unit = unit_model.create_unit_litr()
        my_list.append(item9)

        item10 = nomenclature_model('Белый хлеб')
        item10.group = group_model.create_group('Выпечка')
        item10.unit = unit_model.create_unit_kilogram()
        my_list.append(item10)

        item11 = nomenclature_model('Соль')
        item11.group = group_model.create_group('Приправа')
        item11.unit = unit_model.create_unit_kilogram()
        my_list.append(item11)

        item12 = nomenclature_model('Корица')
        item12.group = group_model.create_group('Приправа')
        item12.unit = unit_model.create_unit_gramm()
        my_list.append(item12)

        item13 = nomenclature_model('Какао')
        item13.group = group_model.create_group('Приправа')
        item13.unit = unit_model.create_unit_kilogram()
        my_list.append(item13)

        item14 = nomenclature_model('Сахарная пудра')
        item14.group = group_model.create_group('Приправа')
        item14.unit = unit_model.create_unit_kilogram()
        my_list.append(item14)

        item15 = nomenclature_model('Лимонный сок')
        item15.group = group_model.create_group('Приправа')
        item15.unit = unit_model.create_unit_millilitr()
        my_list.append(item15)

        item16 = nomenclature_model('Чёрный перец')
        item16.group = group_model.create_group('Приправа')
        item16.unit = unit_model.create_unit_kilogram()
        my_list.append(item16)

        item17 = nomenclature_model('Ванилин')
        item17.group = group_model.create_group('Приправа')
        item17.unit = unit_model.create_unit_kilogram()
        my_list.append(item17)

        return my_list

    @staticmethod
    def create_receipts():
        my_receipts = []

        recipe1 = storage_model('Вафли хрустящие в вафельнице')
        recipe1.add_recipe('Мука', 100, 'gramm')
        recipe1.add_recipe('Сахар', 80, 'gramm')
        recipe1.add_recipe('Сливочное масло', 70, 'gramm')
        recipe1.add_recipe('Яйцо куриное', 1, 'shtuka')
        recipe1.add_recipe('Яйцо куриное', 1, 'shtuka')
        my_receipts.append(recipe1)

        return my_receipts

    def create(self):
        result = []
        if self.__options.is_first_start == True:
            self.__options.is_first_start = False

            # Формируем и зпоминаем номеклатуру
            result = start_factory.create_nomenclature()
            self.__save(storage.nomenclature_key(), result)

        return result