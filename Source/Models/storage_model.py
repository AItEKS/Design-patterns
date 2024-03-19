from Source.abstract_reference import abstract_reference
from Source.exceptions import exception_proxy


class storage_model(abstract_reference):
    _address: str = ""

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str):
        exception_proxy.validate(value, str)
        self._address = value

    @staticmethod
    def create_default() -> abstract_reference:
        storage = storage_model("default")
        storage.address = "г. Москва. ул. Академика Королева, 10"

        return storage
