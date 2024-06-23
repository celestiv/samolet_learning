descr = '''
Замыкание — это способность функции запоминать состояние всех переменных,
 с которыми она работает в ходе своего выполнения, аналогично полям класса.
'''

from typing import Callable, Any 

def multiplier(n: int) -> Callable[...,Any]:
    def mul(k: int) -> int:
        return n * k
    return mul


if __name__ == "__main__":
    mul2 = multiplier(2)
    assert mul2(5) == 10
    assert mul2(11) == 22
