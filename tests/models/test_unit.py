import os
import sys

sys.path.insert(0, os.path.abspath('src'))

from crazy_joe.models import Unit


def test_repr_string_format():
    unit = Unit('cm/s')
    assert(unit.__repr__() == 'Unit(name="cm/s")')
