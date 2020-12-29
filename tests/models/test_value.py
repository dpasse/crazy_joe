import os
import sys
import pytest

sys.path.insert(0, os.path.abspath('src'))

from crazy_joe.models import Value, StaticValue, MinMaxValue, Unit

@pytest.fixture
def unit(tmpdir: str):
    yield Unit('cm/s')

def test_value_repr_string_format(unit):
    value = Value(unit)
    assert(value.__repr__() == 'Value(unit=Unit(name="cm/s"))')

def test_static_value_repr_string_format(unit):
    value = StaticValue('34', unit)
    assert(value.__repr__() == 'StaticValue(value="34", unit=Unit(name="cm/s"))')

def test_min_max_value_repr_string_format(unit):
    value = MinMaxValue(3, 4, unit)
    assert(value.__repr__() == 'MinMaxValue(min=3, max=4, unit=Unit(name="cm/s"))')
