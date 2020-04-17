import json
from json_parser import python_object_to_json


first = (1, [2, 3, {'b': ['a', 'd']}], 4)
second = {'a': [1, (2, 'a', False), (3, 4, 't')], 2: 'b', 3: 'c'}
third = [1, (2, 'a')]
fourth = False
fifth = None
sixth = True
seventh = 34.5
eight = 'hello'
ninth = {1, 2, 3}


def test_json():
    assert str(python_object_to_json(first)) == str(json.dumps(first))
    assert str(python_object_to_json(second)) == str(json.dumps(second))
    assert str(python_object_to_json(third)) == str(json.dumps(third))
    assert str(python_object_to_json(fourth)) == str(json.dumps(fourth))
    assert str(python_object_to_json(fifth)) == str(json.dumps(fifth))
    assert str(python_object_to_json(sixth)) == str(json.dumps(sixth))
    assert str(python_object_to_json(seventh)) == str(json.dumps(seventh))
    assert str(python_object_to_json(eight)) == str(json.dumps(eight))
    assert str(python_object_to_json(ninth)) == '{1, 2, 3}'

    assert str(python_object_to_json(first, 1)) == str(json.dumps(first, indent=4))
    assert str(python_object_to_json(second, 1)) == str(json.dumps(second, indent=4))
    assert str(python_object_to_json(third, 1)) == str(json.dumps(third, indent=4))
    assert str(python_object_to_json(fourth, 1)) == str(json.dumps(fourth, indent=4))
    assert str(python_object_to_json(fifth, 1)) == str(json.dumps(fifth, indent=4))
    assert str(python_object_to_json(sixth, 1)) == str(json.dumps(sixth, indent=4))
    assert str(python_object_to_json(seventh, 1)) == str(json.dumps(seventh, indent=4))
    assert str(python_object_to_json(eight, 1)) == str(json.dumps(eight, indent=4))
    assert str(python_object_to_json(ninth, 1)) == '{\n    1,\n    2,\n    3\n}'

