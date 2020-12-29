from abc import ABC
from typing import List
from ..models import Label


class AbstractLabelFormatter(ABC):
    @property
    def total_width(self):
        pass

    def to_string(self, label: Label) -> List[str]:
        pass
