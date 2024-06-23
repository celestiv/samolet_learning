"""
В данном примере `sleep(0.01)` имитирует переключение контекста операционной системы или
какую-то длительную операцию в треде.
Если запустить пример с закомментированным использованием `Lock`, будет выведен ошибочный результат

state.x = 3 is even

Это происходит, потому что тред, выполняющий функцию `changer` получил управление процессором посреди функции `reader`.
Если же раскомментировать операторы `with state.lock`, код отработает корректно
"""
from threading import Lock, Thread
from time import sleep


class GlobalState:
    def __init__(self, x):
        self.x = x
        self.lock = Lock()

    def set_x(self, x):
        with self.lock:
            self.x = x


def reader(state: GlobalState):
    with state.lock:
        if state.x % 2 == 0:
            sleep(0.1)
            print(f"{state.x=} is even")
        else:
            print(f"{state.x=} is odd")


def changer(state: GlobalState):
    with state.lock:
        state.set_x(state.x + 1)


st = GlobalState(2)
t1 = Thread(target=reader, args=(st,))
t2 = Thread(target=changer, args=(st,))
t1.start()
t2.start()
t1.join()
t2.join()
