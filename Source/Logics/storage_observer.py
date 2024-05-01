from Source.Models.event_type import event_type
from Source.exceptions import exception_proxy, argument_exception, operation_exception

from Source.reference import reference


#
# Наблюдатель для складских операций
#
class storage_observer:
    observers = []

    @staticmethod
    def raise_event(handle_event: str):
        exception_proxy.validate(handle_event, str)
        for object in storage_observer.observers:

            if object is not None:
                object.handle_event(handle_event)

    @staticmethod
    def keys() -> list:
        result = []
        for item in storage_observer.observers:
            result.append(type(item).__name__)

        return result

    @staticmethod
    def get(observer_name: str):
        result = None
        for item in storage_observer.observers:
            if type(item).__name__ == observer_name:
                result = item
                break

        if result == None:
            raise operation_exception(f"Невозможно получить наблюдетель по ключу  {observer_name}!")

        return result

    @staticmethod
    def post_processing_service_key() -> str:
        return "post_processing_service"
