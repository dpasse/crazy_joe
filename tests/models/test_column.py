import os
import sys

sys.path.insert(0, os.path.abspath('src'))

from crazy_joe.models import Column, Label, Value, Unit


def test_repr_string_format():
    column = Column(name='tests', labels=[Label(names=['test'], value=Value(Unit('t')))])
    assert(column.__repr__() == 'Column(name="tests", labels=[Label(names=["test"], value=Value(unit=Unit(name="t")), order=1, importance=1)])')
