from abc import ABC, abstractmethod


class reporting(ABC):
    @abstractmethod
    def create(self, key: str) -> str:
        pass
