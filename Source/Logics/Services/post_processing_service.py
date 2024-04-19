from Source.Logics.Services.service import service
from Source.Models.event_type import event_type
from Source.Logics.storage_observer import storage_observer


class post_processing_service(service):
    def __init__(self, data: list, nomenclature) -> None:
        super().__init__(data)
        self.nomenclature = nomenclature
        storage_observer.observers.append(self)

    def handle_event(self, handle_type: str):
        if handle_type == event_type.nomenclature_deleted():
            self.nomenclature_deleted()

    def nomenclature_deleted(self):
        """
        Удалить номенклатуру из состава рецепта, если она существует.
        Args:
            nomenclature_name (str): Наименование номенклатуры для удаления.
        """
        for recipe in self.data:
            if self.nomenclature.name in recipe._rows:
                del recipe._rows[self.nomenclature.name]
                recipe.__calc_brutto()
