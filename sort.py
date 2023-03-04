import random
from typing import Generator
from loguru import logger
import wait

MAXIMUM_LENGTH = 1000
MAXIMUM_VALUE = 1_000_000


def simulation():
    length, ls = generate_ls()
    ith = random.randint(0, length - 1)
    return find_i_th(ls, ith)


def generate_ls(
    max_length: int = MAXIMUM_LENGTH, maximum_value: int = MAXIMUM_VALUE
) -> tuple[int, Generator[int, None, None]]:
    length = random.randint(1, max_length)
    return length, (random.randint(0, maximum_value) for _ in range(length))


def find_i_th(ls: list[float], ith=int) -> float:
    return _find_i_th(list(ls), ith)


def _find_i_th(ls: list[float], ith: int) -> float:
    wait.wait_a_little()
    if not 0 <= ith < len(ls):
        raise ValueError(f"We dont have {ith=}: 0 <= ith < {len(ls)=}.")
    pivot = ls.pop()
    logger.info("==============")
    logger.info(f"{ls=}")
    logger.info(f"{ith=}")
    logger.info(f"{pivot=}")
    less, greater = [], []
    while ls:
        num = ls.pop()
        if num <= pivot:
            less.append(num)
        else:
            greater.append(num)
    l = len(less)
    if l == ith:
        return pivot
    elif l <= ith:
        return find_i_th(greater, ith - l - 1)
    else:
        return find_i_th(less, ith)
