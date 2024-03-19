from random import randrange

from Source.exceptions import argument_exception, exception_proxy, operation_exception
from Source.abstract_reference import abstract_reference
from Source.Models.storage_model import storage_model
from Source.Models.storage_row_turn_model import storage_row_turn_model
from Source.Storage.storage import storage
from datetime import datetime, timedelta
from Source.Models.nomenclature import nomenclature_model
from Source.Models.unit import unit_model


class storage_row_model(abstract_reference):
    _storage_type: bool = False
    _period: datetime
    _nomenclature: nomenclature_model = None
    _storage: storage_model = None
    _unit: unit_model = None
    _value: float = 0

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float) -> float:
        exception_proxy.validate(value, (float, int))
        if value <= 0:
            raise argument_exception("Некорректно переданы параметры!")

        self._value = value

    @property
    def nomenclature(self) -> nomenclature_model:
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model) -> nomenclature_model:
        exception_proxy.validate(value, nomenclature_model)
        self._nomenclature = value

    @property
    def unit(self) -> unit_model:
        return self._unit

    def unit(self, value: unit_model) -> unit_model:
        exception_proxy.validate(value, unit_model)
        self._unit = value

    def storage(self) -> storage_model:
        return self._storage

    def storage(self, value: storage_model) -> storage_model:
        exception_proxy.validate(value, storage_model)
        self._storage = value

    @property
    def storage_type(self) -> bool:
        return self._storage_type

    @storage_type.setter
    def storage_type(self, value) -> bool:
        if isinstance(value, int):
            self._storage_type = True if value > 0 else False

        elif isinstance(value, bool):
            self._storage_type = value

        else:
            raise argument_exception("Некорректно переданы параметры!")

    @property
    def period(self) -> datetime:
        return self._period

    @period.setter
    def period(self, value: datetime) -> datetime:
        exception_proxy.validate(value, datetime)
        self._period = value

    @staticmethod
    def create_credit_row(nomenclature_name: str, details: list, data: dict, _storage: storage_model) -> reference:
        exception_proxy.validate(nomenclature_name, str)
        exception_proxy.validate(_storage, storage_model)
        if details is None:
            raise argument_exception("Некорректно переданы параметры!")

        if len(details) < 2:
            raise argument_exception("Некорректно переданы параметры!")

        quantity = details[0]
        unit_name = details[1]
        exception_proxy.validate(quantity, (float, int))
        exception_proxy.validate(unit_name, str)

        items = data[storage.nomenclature_key()]
        nomenclatures = abstract_reference.create_dictionary(items)

        keys = list(filter(lambda x: x == nomenclature_name, nomenclatures.keys()))
        if len(keys) == 0:
            raise operation_exception(f"Некоректно передан список. Не найдена номенклатура {nomenclature_name}!")
        nomenclature = nomenclatures[keys[0]]

        items = data[storage.unit_key()]
        units = abstract_reference.create_dictionary(items)

        keys = list(filter(lambda x: x == unit_name, units.keys()))
        if len(keys) == 0:
            raise operation_exception(f"Некорректно передан список. Не найдена единица измерения {unit_name}!")
        unit = units[keys[0]]

        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-02-01", "%Y-%m-%d")

        item = storage_row_model("sample_credit_transaction")
        item.nomenclature = nomenclature
        item.unit = unit
        item.storage_type = True
        item.value = quantity
        item.storage = _storage
        item.period = storage_row_model.random_date(start_date, stop_date)

        return item

    @staticmethod
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
