import pytest
from external_sort import merge_sort


@pytest.fixture(scope='module')
def input_file():
    unsorted_file = 'Tests/test_input.txt'
    sorted_file = 'Tests/sorted_file.txt'
    yield unsorted_file, sorted_file


def test_sort(input_file):
    unsorted_list = list()
    sorted_list = list()

    merge_sort(input_file[0])

    with open(input_file[0], 'r') as unsorted_file:
        for line in unsorted_file:
            unsorted_list.append(int(line))

    with open(input_file[1], 'r') as sorted_file:
        for line in sorted_file:
            sorted_list.append(int(line))

    assert unsorted_list == sorted_list
