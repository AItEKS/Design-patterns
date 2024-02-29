from abc import ABC, abstractmethod
from typing import Dict, List
from collections import defaultdict


class reporting(ABC):
    @abstractmethod
    def create(self, key: str) -> str:
        pass

    @abstractmethod
    def get_classes_fields(self, class_list: List[type]) -> Dict[str, List]:
        classes_fields = defaultdict(list)

        for klass in class_list:
            obj = klass()
            fields = filter(lambda f: not f.startswith("__"), dir(obj.__class__))
            for field in fields:
                classes_fields[klass.__name__.lower()].append(field)

        return dict(classes_fields)
