from Source.abstract_reference import abstract_reference
from Source.exceptions import exception_proxy


class nomenclature_model(abstract_reference):
    " Группа номенклатуры "
    __group = None
    " Единица измерения "
    __unit = None

    @property
    def group(self):
        " Группа номенклатуры "
        return self.__group

    @group.setter
    def group(self, value: abstract_reference):
        " Группа номенклатуры "
        exception_proxy.validate(value, abstract_reference)
        self.__group = value

    @property
    def unit(self):
        " Единица измерения "
        return self.__unit

    @unit.setter
    def unit(self, value: abstract_reference):
        " Единица измерения "
        exception_proxy.validate(value, abstract_reference)
        self.__unit = value