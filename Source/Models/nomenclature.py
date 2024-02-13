from Source.abstract_reference import abstract_reference


class nomenclature(abstract_reference):
    __group = None
    __unit = None
    
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