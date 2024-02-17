from Source.abstract_reference import abstract_reference
from Source.argument_exception import argument_exception


class unit_model(abstract_reference):
    # Инициализация объекта
    def init(self, name, base_unit: str = None, unit_ratio: int = None):
        super().init(name)
        self.base_unit = base_unit
        self.unit_ratio = unit_ratio

    # Геттер и сеттер для поля base_unit
    @property
    def base_unit(self):
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise argument_exception("Некорректная базовая единица!")

        self.__base_unit = value.strip()

    # Геттер и сеттер для поля unit_ratio
    @property
    def unit_ratio(self):
        return self.__unit_ratio

    @unit_ratio.setter
    def unit_ratio(self, value):
        if not isinstance(value, int) or value < 0:
            raise argument_exception("Некорректный коэффициент пересчёта!")

        self.__unit_ratio = value
