from Source.abstract_reference import abstract_reference
from Source.exceptions import exception_proxy, argument_exception


class unit_model(abstract_reference):
    __base_unit: abstract_reference = None
    __coefficient: int = 1

    def __init__(self, name: str, base_unit: abstract_reference = None, coefficient: int = 1):
        super().__init__(name)

        if base_unit != None:
            self.__base_unit = base_unit

        if coefficient != 1:
            self.coefficient = coefficient

    @property
    def base_unit(self):
        return self.__base_unit

    @base_unit.setter
    def base(self, value: abstract_reference):
        exception_proxy.validate(value, abstract_reference)
        self.__base_unit = value

    @property
    def coefficient(self):
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, value: int):
        exception_proxy.validate(value, int)

        if value <= 0:
            raise argument_exception("Значение коэффициента должно быть > 1!")

        self.__coefficient = value

    @staticmethod
    def create_unit_gramm():
        item = unit_model('грамм', None, 1)
        return item

    @staticmethod
    def create_unit_kilogram():
        base = unit_model.create_unit_gramm()
        item = unit_model('килограмм', base, 1000)
        return item

    @staticmethod
    def create_unit_millilitr():
        item = unit_model('миллилитр', None, 1)
        return item

    @staticmethod
    def create_unit_litr():
        base = unit_model.create_unit_millilitr()
        item = unit_model('литр', base, 1000)
        return item

    @staticmethod
    def create_unit_shtuki():
        item = unit_model('штука', None, 1)
        return item