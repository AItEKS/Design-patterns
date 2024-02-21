from Source.abstract_reference import abstract_reference
from Source.exceptions import exception_proxy, argument_exception


#
# Модель единицы измерения для номенклатуры
#
class unit_model(abstract_reference):
    # Базовая единица измерения
    __base_unit: abstract_reference = None

    # Коэффициент пересчета к базовой единице измерения
    __coefficient: int = 1

    def __init__(self, name: str, base_unit: abstract_reference = None, coefficient: int = 1):
        super().__init__(name)

        if base_unit != None:
            self.__base_unit = base_unit

        if coefficient != 1:
            self.coefficient = coefficient

    @property
    def base_unit(self):
        """
            Базовая единица измерения
        Returns:
            _type_: _description_
        """
        return self.__base_unit

    @base_unit.setter
    def base(self, value: abstract_reference):
        exception_proxy.validate(value, abstract_reference)
        self.__base_unit = value

    @property
    def coefficient(self):
        """
            Коэффициент пересчета
        Returns:
            _type_: _description_
        """
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, value: int):
        exception_proxy.validate(value, int)

        if (value <= 0):
            raise argument_exception("Значение коэффициента должно быть > 1!")

        self.__coefficient = value

    @staticmethod
    def create_unit_gramm():
        item = unit_model('gramm', None, 1)
        return item

    @staticmethod
    def create_unit_kilogram():
        base = unit_model.create_unit_gramm()
        item = unit_model('kilogramm', base, 1000)
        return item

    @staticmethod
    def create_unit_millilitr():
        item = unit_model('millilitr', None, 1)
        return item

    @staticmethod
    def create_unit_litr():
        base = unit_model.create_unit_millilitr()
        item = unit_model('litr', base, 1000)
        return item

    @staticmethod
    def create_unit_shtuki():
        item = unit_model('shtuka', None, 1)
        return item