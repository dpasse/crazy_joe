from typing import List
from ..models import Label, Value
from . import AbstractLabelFormatter
from ..utils import list_utils as ListUtils

import numpy as np


class MultiColumnLabelFormatter(AbstractLabelFormatter):
    def __init__(
        self,
        label_column_width: int,
        value_column_width: int
    ):
        self._label_column_width = label_column_width
        self._value_column_width = value_column_width

    @property
    def total_width(self):
        return self._label_column_width + self._value_column_width

    def to_string(self, label: Label) -> List[str]:
        ## label column
        column_1 = self._get_label_column(label)

        ## value / unit column
        column_2 = self._get_unit_column(label.value)

        ## concat
        n_rows: int = np.max([len(column_1), len(column_2)])
        formatted_rows = zip(
            ListUtils.append_empty_rows(ListUtils.ensure_row_width(column_1, self._label_column_width), self._label_column_width, n_rows),
            ListUtils.append_empty_rows(ListUtils.ensure_row_width(column_2, self._value_column_width), self._value_column_width, n_rows),
        )
        return [ f'{col_1}{col_2}' for col_1, col_2 in formatted_rows ]

    def _get_label_column(self, label: Label) -> List[str]:
        current_row_index = 0
        rows = [ label.names[0] ]

        for index in range(1, len(label.names)):
            text = label.names[index]
            value = f'{rows[current_row_index]} {text}'

            if len(value) <= self._label_column_width:
                rows[current_row_index] = value
            else:
                rows.append(text)
                current_row_index += 1

        return rows

    def _get_unit_column(self, value: Value) -> List[str]:
        actual_value = value.get_value()
        if value.is_unitless():
            return [ actual_value ]

        text = f'{actual_value} {value.unit.name}'
        if len(text) <= self._value_column_width:
            return [ text ]

        return [
            actual_value,
            value.unit.name
        ]
