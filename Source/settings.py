class settings:
    def __init__(self):
        self.__report_format = None
        self.__name = ""
        self.__inn = ""
        self.__account = ""
        self.__correspondent_account = ""
        self.__bik = ""
        self.__ownership_type = ""
        self.__first_start = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value.strip(), str):
            raise Exception("Некорректное наименование!")

        self.__name = value.strip()

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 12:
            raise Exception("Некорректный ИНН!")

        self.__inn = value.strip()

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            raise Exception("Некорректный счет!")

        self.__account = value.strip()

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            raise Exception("Некорректный корреспондентский счет!")

        self.__correspondent_account = value.strip()

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 9:
            raise Exception("Некорректный БИК!")

        self.__bik = value.strip()

    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 5:
            raise Exception("Некорректный вид собственности!")

        self.__ownership_type = value.strip()

    @property
    def is_first_start(self):
        return self.__first_start

    @is_first_start.setter
    def is_first_start(self, value: bool):
        self.__first_start = value

    @property
    def report_format(self):
        return self.__report_format

    @report_format.setter
    def report_format(self, value: str):
        valid_formats = ['CSV', 'Markdown', 'Json']

        if value not in valid_formats:
            raise Exception("Некорректный формат отчета!")

        self.__report_format = value
