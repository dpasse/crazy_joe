from typing import List
from . import Column


class Table(object):

    def __init__(self, name: str, columns: List[Column]) -> None:
        self._name = name
        self._columns = columns

    @property
    def name(self):
        return self._name

    @property
    def columns(self):
        return self._columns

    @property
    def number_of_columns(self):
        return len(self._columns)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        columns = ', '.join([ column.__repr__() for column in self.columns ])
        return f'{class_name}(name="{self.name}", columns=[{columns}])'
