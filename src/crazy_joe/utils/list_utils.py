from typing import List


def append_empty_rows(rows: List[str], row_width, n_rows_required: int) -> List[str]:
    while len(rows) < n_rows_required:
        rows.append(' ' * row_width)

    return rows

def ensure_row_width(rows: List[str], width: int) -> List[str]:
    output = []
    for row in rows:
        actual_width = len(row)
        assert(actual_width <= width)

        buffer = (width - actual_width)
        output.append(
            row + (' ' * buffer)
        )

    return output
