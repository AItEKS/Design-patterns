from Source.abstract_reference import abstract_reference


class nomenclature_model(abstract_reference):
    # Инициализация объекта
    def init(self, name):
        super().init(name)
        self.__group = None
        self.__unit = None
        self.__full_name = ""

    # Геттер и сеттер для поля group
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: abstract_reference):
        if value != None:
            self.error.set_error_source("Некорректно указана группа!", self)
        self.__group = value

    # Геттер и сеттер для поля unit
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value: abstract_reference):
        if value != None:
            self.error.set_error_source("Некорректно указана единица измерения!", self)
        self.__unit = value

    # Геттер и сеттер для поля full_name
    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        if len(value) > 255:
            self.error.set_error_source("Превышена максимальная длина для полного наименования!", self)
        self.__full_name = value
