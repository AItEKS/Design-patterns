from Source.abstract_reference import abstract_reference


class nomenclature(abstract_reference):
    def __init__(self, name):
        super().__init__(name)
        self.__group = ""
        self.__unit = ""
        self.__full_name = ""

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: abstract_reference):
        if value == "":
            self.error.set_error_source("Некорректно указана группа", self)

        self.__group = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value: abstract_reference):
        if value == "":
            self.error.set_error_source("Некорректно указана единица измерения", self)

        self.__unit = value

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        if len(value) > 255:
            self.error.set_error_source("Превышена максимальная длина для полного наименования", self)

        self.__full_name = value
