from datetime import datetime

from Source.Models.unit import unit_model
from Source.Models.nomenclature import nomenclature_model


class storage_turn_model:
    def __init__(self):
        self.__storage_name = None
        self.__turnover = None
        self.__nomenclature = None
        self.__unit = None
        self.__period = None

    @property
    def storage_name(self):
        return self.__storage_name

    @storage_name.setter
    def storage_name(self, value: str):
        self.__storage_name = value

    @property
    def turnover(self):
        return self.__turnover

    @turnover.setter
    def turnover(self, value: int):
        self.__turnover = value

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        self.__nomenclature = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value: unit_model):
        self.__unit = value

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value: datetime):
        self.__period = value
