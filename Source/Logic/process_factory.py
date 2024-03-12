from Source.Logic.process_storage_turn import process_storage_turn
from Source.exceptions import operation_exception


class process_factory:
    def create_process(self, process_type: str):
        if process_type == 'storage_turn':
            return process_storage_turn()

        else:
            raise operation_exception("Неподдерживаемый тип процесса")

