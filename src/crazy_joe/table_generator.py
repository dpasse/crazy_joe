import re
from .models import Table
from .formatters import AbstractLabelFormatter
from .utils import list_utils as ListUtils
from typing import Dict
import numpy as np


class TableGenerator(object):

    def __init__(
      self,
      column_formatters: Dict[str, AbstractLabelFormatter],
      append_headers: bool = False
    ):
        self._column_formatters = column_formatters
        self._append_headers = append_headers

    def generate(self, table: Table):
        table_columns = []
        for column in table.columns:
            formatter = self._column_formatters[column.name]

            table_column = []
            if self._append_headers:
              table_column.append(
                ListUtils.ensure_row_width([ column.name ], formatter.total_width)[0]
              )

            for label in column.labels:
                table_column.extend(
                   formatter.to_string(label),
                )

            table_columns.append(table_column)

        formatted_table_columns = []
        n_table_rows = np.max([ len(column) for column in table_columns ])
        for ci, column in enumerate(table.columns):
            column_rows = ListUtils.append_empty_rows(
                table_columns[ci],
                self._column_formatters[column.name].total_width,
                n_table_rows
            )

            formatted_table_columns.append(column_rows)

        rows = []
        for i in range(n_table_rows):
            row_text = ''
            for values in formatted_table_columns:
                row_text += values[i]

            rows.append(re.sub(r'\s+$', '', row_text))

        return '\n'.join(rows)
