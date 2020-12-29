import os
import sys

sys.path.insert(0, os.path.abspath('src'))

from crazy_joe.models import Label, Value, Unit


def test_repr_string_format_with_no_unit():
    label = Label(names=['H'], value=Value(None))
    assert(label.__repr__() == 'Label(names=["H"], value=Value(unit=None), order=1, importance=1)')

def test_repr_string_format_with_unit():
    label = Label(names=['H'], value=Value(Unit('h')))
    assert(label.__repr__() == 'Label(names=["H"], value=Value(unit=Unit(name="h")), order=1, importance=1)')

def test_repr_string_format_with_multiple_names():
    label = Label(names=['H', 'E'], value=Value(Unit('h')))
    assert(label.__repr__() == 'Label(names=["H", "E"], value=Value(unit=Unit(name="h")), order=1, importance=1)')

