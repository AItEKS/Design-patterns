from Source.Logics.Services.service import service
from Source.exceptions import exception_proxy, operation_exception
from Source.reference import reference
from Source.Logics.storage_observer import storage_observer
from Source.Models.event_type import event_type
from Source.Logics.Services.post_processing_service import post_processing_service
from Source.LogEntry import LogEntry


#
# Сервис для выполнения CRUD операций
#
class reference_service(service):

    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.observers.append(self)
        post_processing_service(self.data)

    def add(self, item: reference) -> bool:
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id, self.data))
        if len(found) > 0:
            return False

        self.data.append(item)
        storage_observer.raise_event(event_type.log_entry(LogEntry("DEBUG", f"Adding reference: {item.id}")))
        return True

    def delete(self, item: reference) -> bool:
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id, self.data))
        if len(found) == 0:
            return False
        item = found[0]

        observer_item = storage_observer.get(storage_observer.post_processing_service_key())
        observer_item.nomenclature = item
        storage_observer.raise_event(event_type.deleted_nomenclature())

        self.data.remove(item)
        storage_observer.raise_event(event_type.log_entry(LogEntry("DEBUG", f"Delete reference: {item.id}")))
        return True

    def change(self, item: reference) -> bool:
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id, self.data))
        if len(found) == 0:
            return False

        self.delete(found[0])
        self.add(item)
        storage_observer.raise_event(event_type.log_entry(LogEntry("DEBUG", f"Changed reference: {item.id}")))
        return True

    def get(self) -> list:
        return self.data

    def get_item(self, id: str) -> reference:
        exception_proxy.validate(id, str)
        found = list(filter(lambda x: x.id == id, self.data))
        if len(found) == 0:
            raise operation_exception(f"Не найден элемент с кодом {id}!")

        storage_observer.raise_event(event_type.log_entry(LogEntry("DEBUG", f"Got reference: {found}")))
        return found

    def handle_event(self, handle_type: str):
        super().handle_event(handle_type)