import pytest

import sort


@pytest.fixture
def array_1():
    return [1]


@pytest.fixture
def array_2():
    return [2, 1]


max_length, max_value = 10, 100
min_length = 5


@pytest.fixture
def array_random():
    length = None
    while (not length) or (length < min_length):
        length, array = sort.create_generator(max_length, max_value)
    return length, array


class TestCreateGenerator:
    def test_create_generator_length(self, array_random):
        length, _ = array_random
        assert 0 < length <= max_length

    def test_create_generator_value(self, array_random):
        _, generator = array_random
        assert all(0 <= val <= max_value for val in generator)

    def test_create_generator_length_is_consistent(self, array_random):
        length, generator = array_random
        assert len(list(generator)) == length


class TestFindIthInput:
    def test_find_ith_raises_error_empty_array(self):
        with pytest.raises(ValueError):
            sort.find_i_th([], 10)

    def test_find_ith_raises_error_ith_negative(self):
        with pytest.raises(ValueError):
            sort.find_i_th([10, 10, 10], -1)


class TestFindIthReturn:
    def test_find_ith_array_1(self, array_1):
        assert sort.find_i_th(array_1, 0) == 1

    def test_find_ith_array_2(self, array_2):
        assert sort.find_i_th(array_2, 0) == 1
        assert sort.find_i_th(array_2, 1) == 2

    def test_find_ith_array(self, array_random):
        array_random = list(array_random[1])
        solution = sorted(array_random)
        for i, val in enumerate(solution):
            assert val == sort.find_i_th(array_random, i)
