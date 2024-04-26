from Source.Models.event_type import event_type
from Source.exceptions import exception_proxy
from Source.Logics.Services.reference_service import reference_service


#
# Наблюдатель для складских операций
#
class storage_observer:
    observers = []

    @staticmethod
    def raise_event(handle_event: str):
        """
            Сформировать события
        Args:
            handle_event (str): _description_
        """
        exception_proxy.validate(handle_event, str)
        for object in storage_observer.observers:

            if object is not None:
                object.handle_event(handle_event)
