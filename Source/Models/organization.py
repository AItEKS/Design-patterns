from Source.abstract_reference import abstract_reference
from Source.settings import settings
from Source.argument_exception import argument_exception


class organization_model(abstract_reference):
    # ИНН организации
    inn = ""
    # БИК банка
    __bik = ""
    # Номер счета
    __account = ""
    # Вид собственности
    __ownership_type = ""

    def __init(self, name):
        super().init(name)
        self.__settings = settings()

    def set_settings(self, settings):
        self.__settings = settings

    # Геттер и сеттер для ИНН
    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 12:
            raise argument_exception("Некорректный ИНН!")

        self.__inn = value.strip()

    # Геттер и сеттер для номера счета
    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            raise argument_exception("Некорректный счет!")

        self.__account = value.strip()

    # Геттер и сеттер для БИК
    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 9:
            raise argument_exception("Некорректный БИК!")

        self.__bik = value.strip()

    # Геттер и сеттер для вида собственности
    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 5:
            raise argument_exception("Некорректный вид собственности!")

        self.__ownership_type = value.strip()
