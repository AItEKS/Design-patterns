from Source.Logics.Services.service import service
from Source.Models.event_type import event_type
from Source.Logics.storage_observer import storage_observer


class post_processing_service(service):
    observers = []

    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.observers.append(self)

    @staticmethod
    def raise_event(handle_event: str):
        for observer in storage_observer.observers:
            observer.handle_event(handle_event)

    def handle_event(self, handle_type: str):
        if handle_type == event_type.nomenclature_deleted():
            # Реализация удаления
            pass