from Source.abstract_reference import abstract_reference


class unit(abstract_reference):
    def __init__(self, name, base_unit: str = None, unit_ratio: str = None):
        super().__init__(name)
        self.__base_unit = base_unit
        self.__unit_ratio = unit_ratio

    @property
    def base_unit(self):
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value):
        self.__base_unit = value

    @property
    def unit_ratio(self):
        return self.unit_ratio

    @unit_ratio.setter
    def unit_ratio(self, value):
        self.unit_ratio = value
