import pytest
import json
from json_parser import python_object_to_json


first = (1, [2, 3, {'b': ['a', 'd']}], 4)
second = {'a': [1, (2, 'a', False), (3, 4, 't')], 2: 'b', 3: 'c'}
third = [1, (2, 'a')]


@pytest.mark.parametrize(
    'obj, result',
    [
        (first, json.dumps(first)),
        (second, json.dumps(second)),
        (third, json.dumps(third))
    ]
)
def test(obj, result):
    assert python_object_to_json(obj) == result
