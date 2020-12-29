import os
import sys
import pytest

sys.path.insert(0, os.path.abspath('src'))

from crazy_joe.models import Table, Column, Label, StaticValue, Unit
from crazy_joe.formatters import HorizontalLabelFormatter, MultiColumnLabelFormatter
from crazy_joe import TableGenerator

@pytest.fixture
def table(tmpdir: str):
    table = Table(
        name='abc',
        columns=[
            Column(
                '1',
                labels=[
                    Label(names=['Study', 'Time:'], value=StaticValue('120', unit=Unit('mins'))),
                    Label(names=['Exercise', 'Time:'], value=StaticValue('1', unit=Unit('hrs'))),
                    Label(names=['School', 'Time:'], value=StaticValue('8', unit=Unit('hrs'))),
                ]
            ),
            Column(
                '2',
                labels=[
                    Label(names=['Car', 'Speed:'], value=StaticValue('72', unit=Unit('mph'))),
                    Label(names=['Bike', 'Speed:'], value=StaticValue('22', unit=Unit('mph'))),
                ]
            )
        ],
    )

    yield table

def test_horizontal_formatted_table(table):
    expected_table = '1                        2\n'
    expected_table += 'Study Time: 120 mins     Car Speed: 72 mph\n'
    expected_table += 'Exercise Time: 1 hrs     Bike Speed: 22 mph\n'
    expected_table += 'School Time: 8 hrs'

    formatter = HorizontalLabelFormatter(25)
    generator = TableGenerator({ '1': formatter, '2': formatter }, True)
    output = generator.generate(table)
    assert(expected_table == output)

def test_horizontal_formatted_multiple_lines_table(table):
    expected_table = 'Study Time: 120    Car Speed: 72 mph\n'
    expected_table += 'mins               Bike Speed: 22 mph\n'
    expected_table += 'Exercise Time: 1\n'
    expected_table += 'hrs\n'
    expected_table += 'School Time: 8 hrs'

    formatter = HorizontalLabelFormatter(19)
    generator = TableGenerator({ '1': formatter, '2': formatter })
    output = generator.generate(table)
    assert(expected_table == output)

def test_multi_column_formatted_table(table):
    expected_table = 'Study Time:       120 mins  Car Speed:        72 mph\n'
    expected_table += 'Exercise Time:    1 hrs     Bike Speed:       22 mph\n'
    expected_table += 'School Time:      8 hrs'


    formatter = MultiColumnLabelFormatter(18, 10)
    generator = TableGenerator({ '1': formatter, '2': formatter })
    output = generator.generate(table)

    assert(expected_table == output)

def test_multiple_formatters_table(table):
    expected_table = 'Study Time:       120 mins  Car Speed: 72\n'
    expected_table += 'Exercise Time:    1 hrs     mph\n'
    expected_table += 'School Time:      8 hrs     Bike Speed: 22\n'
    expected_table += '                            mph'

    generator = TableGenerator({ '1': MultiColumnLabelFormatter(18, 10), '2': HorizontalLabelFormatter(15) })
    output = generator.generate(table)

    assert(expected_table == output)
