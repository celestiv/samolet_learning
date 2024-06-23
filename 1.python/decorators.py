# Декоратор — это обертка вокруг функции или класса, которая изменяет или расширяет их поведение. 
# Он особенно эффективен, когда пользователю необходимо модифицировать результат функции или 
# выполнить дополнительные действия.
from typing import Callable
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def plus_2(func: Callable) -> Callable:
    def wrapper():
        result = func()
        return result + 2
    return wrapper


def get_three():
    return 3


def get_four():
    return 4


@plus_2
def get_five():
    return 5


if __name__ == "__main__":
    logging.info(plus_2(get_three)())
    logging.debug(plus_2(get_four)())
    logging.debug(get_five())
