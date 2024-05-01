from Source.Logics.Services.service import service
from Source.Models.event_type import event_type
from Source.Models.nomenclature_model import nomenclature_model
from Source.exceptions import exception_proxy
from Source.Logics.storage_observer import storage_observer
from Source.Models.nomenclature_model import nomenclature_model
from Source.Storage.storage import storage


class post_processing_service(service):
    __nomenclature: nomenclature_model = None

    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.observers.append(self)

    @property
    def nomenclature(self) -> nomenclature_model:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, source: nomenclature_model):
        exception_proxy.validate(source, nomenclature_model)
        self.__nomenclature = source

    def __observe_deleted_nomenclature(self):
        if self.__nomenclature is None:
            return

        data_storage = storage()
        key = storage.receipt_key()
        receipts = data_storage.data[key]

        for receipt in receipts:
            keys = list(receipt.consist.keys())
            for key in keys:
                row = receipt.consist[key]
                if row.nomenclature.id == self.__nomenclature.id:
                    receipt.delete(row)

    def handle_event(self, handle_type: str):
        """
            Обработать событие
        Args:
            handle_type (str): _description_
        """
        super().handle_event(handle_type)

        if handle_type == event_type.deleted_nomenclature():
            self.__observe_deleted_nomenclature()