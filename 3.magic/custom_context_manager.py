"""
Протокол менеджера контекста состоит из двух методов: `__enter__()` и `__exit__()`.

Первый метод `__enter__(self)` не имеет входных параметров. Он вызывается после вычисления выражения `expression`,
и его результат присваивается переменной `target`, если имя переменной выбрано после ключевого слова `as`.

Метод `__exit__(self, exc_type, exc_value, traceback)` принимает на вход параметры исключения, которое возникло
в процессе выполнения кода, обернутого менеджером контекста. К этим параметрам относятся: тип исключения,
сам объект исключения и `traceback`, содержащий информацию о последовательности вызовов, предшествующих исключению.
Если исключение не возникло, все три аргумента принимают значение `None`. Метод `_exit_()` вызывается в конце блока кода
"""


class SimpleContextManager:
    """
    В этом примере:
    Метод `__enter__` выводит сообщение и возвращает строку "Hello, World!",
        которая затем присваивается переменной `value`.
    Метод `__exit__` обрабатывает завершение контекста, выводя сообщение о выходе.
        Если в блоке `with` возникает исключение, метод `__exit__` также выводит информацию об этом исключении.
    Внутри блока `with` мы просто печатаем значение, возвращаемое `__enter__`.
    """
    def __enter__(self):
        print("Entering the context")
        return "Hello from context"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception occured: {exc_type}")
        print("Exiting the context")


with SimpleContextManager() as scm:
    print(scm)



from contextlib import contextmanager


@contextmanager
def open_file(name):
    filename = None
    try:
        filename = open(name, "r")
        yield filename
    finally:
        filename.close()


with open_file("1.txt") as f:
    f.read()
