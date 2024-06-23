from typing import Any, Callable
import logging



def square(degree: int) -> Callable[...,Any]:
    delta = 0
    def wrapper(val: int) -> int:
        nonlocal delta
        result = pow(val, degree + delta)
        delta += 1
        return result
    return wrapper   


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    to_square = square(2)
    logging.info(to_square(7))
    logging.info(to_square(7))
    logging.info(to_square(7))
