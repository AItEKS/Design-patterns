import abc
from Source.errors import error_proxy
from Source.exceptions import argument_exception


class processing(error_proxy):

    @abc.abstractmethod
    def process(self, transactions: list) -> list:
        if transactions == None:
            raise argument_exception("Некорректно передан параметр!")

        if len(transactions) == 0:
            raise argument_exception("Некорректно передан параметр!")

        self.clear()