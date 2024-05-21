from typing import Any
import logging


class ToPowerWithDelta:
    '''
        Функторы — объекты, которые можно вызывать подобно функциям. 
        Они поддерживают операцию вызова `__call__()`. 
        Это позволяет создавать функции, 
        которые умеют хранить свое состояние от вызова к вызову.
    '''
    def __init__(self, val1: int):
        self.val1 = val1
        self.delta = 0

    def __call__(self, val2) -> Any:
        result = pow(val2, self.val1 + self.delta)
        self.delta += 1
        return result
    
class ToPowerWithOtherDelta(ToPowerWithDelta):
    '''
        В полученной записи мы модифицировали исходный пример. 
        Теперь значение свойства `delta` изменяется в отдельном методе `get_delta()`.
        В этой версии кода, чтобы изменить логику вычисления `delta`, 
        нам достаточно создать подкласс от уже существующего функтора и 
        определить в нем новый алгоритм вычисления свойства `delta`.
    '''
    def __init__(self, val1: int):
        super().__init__(val1)
        self.delta = 2
    
    def get_delta(self):
        result = self.delta
        self.delta *= 2
        return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    to_square = ToPowerWithDelta(3)
    logging.info(to_square(7))
    logging.info(to_square(7))

    to_square_other = ToPowerWithOtherDelta(2)
    logging.info(to_square_other(7))
    logging.info(to_square_other(7))
