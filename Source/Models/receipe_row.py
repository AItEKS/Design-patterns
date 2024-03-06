from Source.abstract_reference import abstract_reference
from Source.Models.nomenclature import nomenclature_model
from Source.Models.unit import unit_model
from Source.exceptions import exception_proxy


class receipe_row_model(abstract_reference):
    __nomenclature: nomenclature_model = None
    __size: int = 0
    __unit: unit_model = None

    def __init__(self, __nomenclature: nomenclature_model, __size: int, __unit: unit_model):
        exception_proxy.validate(__nomenclature, abstract_reference)
        exception_proxy.validate(__unit, abstract_reference)

        self.__nomenclature = __nomenclature
        self.__size = __size
        self.__unit = __unit

        super().__init__(f"{__nomenclature.name} , {__unit.name} ")

    @property
    def nomenclature(self):
        return self.__nomenclature

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: int):
        self.__size = value

    @property
    def unit(self):
        return self.__unit
