import os
import sys

sys.path.insert(0, os.path.abspath('src'))

from crazy_joe.models import Label, StaticValue, Unit
from crazy_joe.formatters import MultiColumnLabelFormatter


def test_single_label():
    label =Label(
      names=['speed'],
      value=StaticValue('3', Unit('cm'))
    )

    formatter = MultiColumnLabelFormatter(15, 8)
    label_rows = formatter.to_string(label)

    assert(len(label_rows) == 1)
    assert(label_rows[0] == 'speed' + (' ' * 10) + '3 cm' + (' ' * 4))

def test_single_label_multiple_lines():
    label =Label(
      names=['speed', 'of', 'flight'],
      value=StaticValue('3', Unit('cm'))
    )

    formatter = MultiColumnLabelFormatter(10, 8)
    label_rows = formatter.to_string(label)

    assert(len(label_rows) == 2)
    assert(label_rows[0] == 'speed of' + (' ' * 2) + '3 cm' + (' ' * 4))
    assert(label_rows[1] == 'flight' + (' ' * 4) + (' ' * 8))
