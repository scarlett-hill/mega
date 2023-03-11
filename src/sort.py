import functools
import array
import random
import typing

from loguru import logger

import wait

MINIMUM_LENGTH = 1
MAXIMUM_LENGTH = 1000
MAXIMUM_VALUE = 1_000_000

array_integer = functools.partial(array.array, "I")
Size = int
Value = int


def simulate() -> Value:
    length, generator = create_generator(MINIMUM_LENGTH, MAXIMUM_LENGTH, MAXIMUM_VALUE)
    ith = random.randint(0, length - 1)
    return find_i_th(generator, ith)


def create_generator(
    min_length: Size, max_length: Size, maximum_value: Value
) -> tuple[Size, typing.Generator[Value, None, None]]:
    length = random.randint(min_length, max_length)
    return length, (random.randint(0, maximum_value) for _ in range(length))


def find_i_th(generator: typing.Generator[Value, None, None], ith: Size) -> Value:
    arr = array_integer(generator)
    original_length = len(arr)
    result, n_step = _find_i_th(arr, ith)
    logger.info(
        f"""The array was {original_length}-long.
            It took {n_step} steps to reach {ith}-th.
            Here is the result: {result}."""
    )
    return result


def _find_i_th(arr: array_integer(), ith: Size, n_step: int = 0) -> tuple[Value, int]:
    wait.wait_a_little()
    if not 0 <= ith < len(arr):
        raise ValueError(f"We dont have {ith=}: 0 <= ith < {len(arr)=}.")
    pivot = arr.pop()
    log_state(arr, ith, pivot)
    less, greater = array_integer(), array_integer()
    while arr:
        num = arr.pop()
        if num <= pivot:
            less.append(num)
        else:
            greater.append(num)
    l = len(less)
    if l < ith:
        return _find_i_th(greater, ith - l - 1, n_step + 1)
    elif ith < l:
        return _find_i_th(less, ith, n_step + 1)
    elif l == ith:
        return pivot, n_step


def log_state(ls: array_integer(), ith: Size, pivot: Value) -> None:
    logger.debug("==============")
    logger.debug(f"{ls=}")
    logger.debug(f"{ith=}")
    logger.debug(f"{pivot=}")
