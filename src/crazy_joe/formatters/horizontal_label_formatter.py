from typing import List
from ..models import Label
from . import AbstractLabelFormatter
from ..utils import list_utils as ListUtils


class HorizontalLabelFormatter(AbstractLabelFormatter):
    def __init__(
        self,
        width: int
    ):
        self._width = width

    @property
    def total_width(self):
        return self._width

    def to_string(self, label: Label) -> List[str]:
        ## name
        parts = label.names

        ## value
        parts.append(label.value.get_value())

        ## unit
        if not label.value.is_unitless():
            parts.append(label.value.unit.name)

        return ListUtils.ensure_row_width(
            self._get_column(parts),
            self._width
        )

    def _get_column(self, parts: str) -> List[str]:
        current_row_index = 0
        rows = [ parts[0] ]

        for index in range(1, len(parts)):
            part = parts[index]

            value = f'{rows[current_row_index]} {part}'
            if len(value) <= self._width:
                rows[current_row_index] = value
            else:
                rows.append(part)
                current_row_index += 1

        return rows
