from . import Unit
from typing import Optional

import numpy as np


class Value(object):
    def __init__(self, unit: Optional[Unit]) -> None:
        self._unit = unit

    @property
    def unit(self):
        return self._unit

    def is_unitless(self):
        return self._unit == None

    def get_value(self) -> str:
        random_value = np.random.rand()
        return str(round(random_value, 2))

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        if self.is_unitless():
            return f'{class_name}(unit=None)'

        return f'{class_name}(unit={self._unit.__repr__()})'

class StaticValue(Value):
    def __init__(self, value: str, unit: Optional[Unit]) -> None:
        super().__init__(unit)

        self._value = value

    def get_value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        if self.is_unitless():
            return f'{class_name}(value={self._value}, unit=None)'

        return f'{class_name}(value="{self._value}", unit={self._unit.__repr__()})'

class MinMaxValue(Value):
    def __init__(self, min: int, max: int, unit: Optional[Unit]) -> None:
        super().__init__(unit)

        self._min = min
        self._max = max

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    def get_value(self) -> str:
        random_value = np.random.uniform(self.min, self.max, 1)[0]
        return str(round(random_value, 2))

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        if self.is_unitless():
            return f'{class_name}(min={self.min}, max={self.max}, unit=None)'

        return f'{class_name}(min={self.min}, max={self.max}, unit={self._unit.__repr__()})'
