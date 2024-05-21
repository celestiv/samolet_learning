from typing import Any, Callable
import logging


class Validation:
    '''
        создаем класс функтор и используем его как декоратор
    '''
    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

    def __call__(self, arg: Callable[...,Any]) -> Callable[...,Any]:
        def wrapper(a: int) -> int:
            res = arg(a)
            if not self.lower < res < self.upper:
                raise ValueError("Validation failed")
            return res
        return wrapper
    

@Validation(0, 10)
def square(a):
    return a ** 2


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    to_square = square(2)
    logging.info(square(2))

