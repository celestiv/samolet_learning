from typing import Any
import logging


class ArithmeticProgression:
    def __init__(self, init_val: int, step: int) -> None:
        self.init_val = init_val
        self.step = step

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        result = self.init_val
        self.init_val += self.step
        return result
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    prog = ArithmeticProgression(5, 2)
    logging.info(prog())
    logging.info(prog())
    logging.info(prog())
    logging.info(prog())
