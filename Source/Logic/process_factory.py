from Source.Logic.process_storage_turn import process_storage_turn
from Source.exceptions import operation_exception, exception_proxy


class process_factory:
    __maps = {}

    def __init__(self):
        self.__build_structure()

    def __build_structure(self):
        self.__maps["storage_turn"] = process_storage_turn

    def create(self, process_type: str, transactions: list):
        exception_proxy.validate(process_type, str)
        exception_proxy.validate(transactions, list)

        if not transactions:
            raise operation_exception("Список транзакций пуст")

        if process_type not in self.__maps.keys():
            raise operation_exception(f"Тип процесса {process_type} не поддерживается")

        process_class = self.__maps[process_type]
        result = process_class.process_storage_turn(transactions)

        return result

