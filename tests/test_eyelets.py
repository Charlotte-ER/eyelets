import pytest
import sys

sys.path.append('../src/eyelets')
from eyelets import calculate_standard_distance_between_eyelets, title, create_instructions, create_diagram


def test_calculate_standard_distance_between_eyelets():
    assert calculate_standard_distance_between_eyelets(10, 1, 6) == 1.2
    with pytest.raises(TypeError):
        assert calculate_standard_distance_between_eyelets('foo', 1, 6)
    

def test_title():
    assert title('test') == f'\n{"-" * 100} \nTEST\n{"-" * 100}\n\n'
    with pytest.raises(AttributeError):
        assert title(1001)


def test_create_instructions():
    assert len(create_instructions(10, 1, 1.2, 6)) == 886


def test_create_diagram():
    len(create_diagram(1.2, 6)) == 476