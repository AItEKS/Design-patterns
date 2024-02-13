from Source.abstract_reference import abstract_reference
from Source.settings import settings
from Source.argument_exception import argument_exception

class organization(abstract_reference):
    __inn = ""
    __bik = ""
    __account = ""
    __ownership_type = ""

    def __init__(self, name):
        super().__init__(name)

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 12:
            raise argument_exception("Некорректный ИНН!")

        self.__inn = value.strip()

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            raise argument_exception("Некорректный счет!")

        self.__account = value.strip()

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 9:
            raise argument_exception("Некорректный БИК!")

        self.__bik = value.strip()

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 5:
            raise argument_exception("Некорректный вид собственности!")

        self.__ownership_type = value.strip()
