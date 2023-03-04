import time
import random
from loguru import logger

MAX_SLEEP = 15
SMALL_WAIT = 5


def wait(n: int) -> None:
    time.sleep(random.randrange(MAX_SLEEP))
    logger.info(f"Python is calling me for the {n}-th time.")


def wait_a_little() -> None:
    time.sleep(SMALL_WAIT)
