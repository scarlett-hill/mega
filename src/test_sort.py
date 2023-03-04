import pytest

import sort


@pytest.fixture
def array_1():
    return [1]


@pytest.fixture
def array_2():
    return [2, 1]


max_length, max_value = 10, 100


@pytest.fixture
def array_random():
    return sort.create_generator(max_length, max_value)


def test_create_generator_length(array_random):
    length, _ = array_random
    assert 0 < length <= max_length


def test_create_generator_value(array_random):
    _, generator = array_random
    assert all(0 <= val <= max_value for val in generator)
