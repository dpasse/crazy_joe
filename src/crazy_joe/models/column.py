from typing import List
from . import Label


class Column(object):
    def __init__(self, name: str, labels: List[Label] = []) -> None:
        self._name = name
        self._labels = labels

    @property
    def name(self):
        return self._name

    @property
    def labels(self):
        return self._labels

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        labels = ', '.join([ label.__repr__() for label in self.labels ])
        return f'{class_name}(name="{self.name}", labels=[{labels}])'
