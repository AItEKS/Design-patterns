from Source.abstract_reference import abstract_reference
from Source.Models.receipe_row import receipe_row_model
from Source.exceptions import exception_proxy, operation_exception, argument_exception


class receipe_model(abstract_reference):
    __brutto: int = 0
    __netto: int = 0
    __rows = {}

    def add(self, row: receipe_row_model):
        exception_proxy.validate(row, receipe_row_model)
        self.__rows[row.name] = row
        self.__calc_brutto()

    def delete(self, row: receipe_row_model):
        exception_proxy.validate(row, receipe_row_model)

        if row.name in self.__rows.keys():
            self.__rows.pop(row.name)

        self.__calc_brutto()

    def __calc_brutto(self):
        self.__brutto = 0
        for position in self.__rows:
            self.__brutto += self.__rows[position].size

    @property
    def netto(self):
        return self.__netto

    @netto.setter
    def netto(self, value: int):
        exception_proxy.validate(value, int)

        self.__netto = value

    @staticmethod
    def create_receipt(name: str, comments: str, items: list, data: list):
        exception_proxy.validate(name, str)
        if len(items) == 0:
            raise argument_exception(f"Некорректно передан параметр {items}. Список пуст!")

        nomenclatures = abstract_reference.create_dictionary(data)

        receipt = receipe_model(name)

        for position in items:
            __list = list(position.items())
            if len(__list) < 1:
                raise operation_exception(
                    "Невозможно сформировать элементы рецепта! Некорректный список исходных элементов!")

            tuple = list(__list)[0]
            if len(tuple) < 2:
                raise operation_exception("Невозможно сформировать элемент рецепта. Длина кортежа не корректна!")

            nomenclature_name = tuple[0]
            size = tuple[1]

            keys = list(filter(lambda x: x == nomenclature_name, nomenclatures.keys()))
            if len(keys) == 0:
                raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")

            nomenclature = nomenclatures[nomenclature_name]

            if nomenclature.unit.base_unit is None:
                unit = nomenclature.unit
            else:
                unit = nomenclature.unit.base_unit

            row = receipe_row_model(nomenclature, size, unit)
            receipt.add(row)

        return receipt