class storage:
    __data = ()
    __nomenclature = "nomenclature"
    __group_key = "group_key"
    __unit_key = "unit_key"
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance

    def data(self) -> dict:
        return self.__data

    @staticmethod
    def nomenclature_key():
        return "nomenclature"

    @staticmethod
    def group_key():
        return "group"

    @staticmethod
    def unit_key():
        return "unit"