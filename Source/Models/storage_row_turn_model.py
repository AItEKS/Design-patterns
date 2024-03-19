from Source.abstract_reference import abstract_reference
from Source.exceptions import exception_proxy, argument_exception
from Source.Models.nomenclature import nomenclature_model
from Source.Models.storage_model import storage_model
from Source.Models.unit import unit_model


class storage_row_turn_model(abstract_reference):
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

    @staticmethod
    def create(nomenclature: nomenclature_model, storage: storage_model, unit: unit_model) -> reference:
        row = storage_row_turn_model("-")
        row.storage = storage
        row.unit = unit
        row.nomenclature = nomenclature

        return row
