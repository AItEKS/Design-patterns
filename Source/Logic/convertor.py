from abc import ABC, abstractmethod


class convertor(ABC):
    @abstractmethod
    def convert(self, obj):
        pass
