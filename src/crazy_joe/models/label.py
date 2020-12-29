from . import Value
from typing import List


class Label(object):
    def __init__(self, names: List[str], value: Value, order: int = 1, importance: int = 1) -> None:
        self._names = names
        self._value = value
        self._order = order
        self._importance = importance

    @property
    def names(self):
        return self._names

    @property
    def value(self):
        return self._value

    @property
    def order(self):
        return self._order

    @property
    def importance(self):
        return self._importance

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        names = ', '.join([ f'"{name}"' for name in self.names ])
        return f'{class_name}(names=[{names}], value={self._value.__repr__()}, order={self.order}, importance={self.importance})'

    def __str__(self) -> str:
        return ' '.join(self.names)
