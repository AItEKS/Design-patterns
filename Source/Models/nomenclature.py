from Source.abstract_reference import abstract_reference
from Source.exceptions import exception_proxy


class nomenclature_model(abstract_reference):
    __group = None
    __unit = None

    def __init__(self, name: str, group: abstract_reference = None, unit: abstract_reference = None):
        exception_proxy.validate(group, abstract_reference)
        exception_proxy.validate(unit, abstract_reference)

        self.__group = group
        self.__unit = unit
        super().__init__(name)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: abstract_reference):
        exception_proxy.validate(value, abstract_reference)
        self.__group = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value: abstract_reference):
        exception_proxy.validate(value, abstract_reference)
        self.__unit = value