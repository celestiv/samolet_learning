"""
Оператор `with` упрощает работу с файлами, автоматически их закрывая. При работе с каким-то другим ресурсом,
если его API также предоставляет метод `close()` для освобождения ресурса, можно получить аналогичное поведение,
используя менеджер контекста `contextlib.closing`.
Рассмотрим подключение к базе данных SQLite на примере встроенной библиотеки sqlite3:

В этом примере мы создаем подключение к базе данных SQLite в оперативной памяти, используя метод `connect()`
из модуля `sqlite3`. Затем мы используем менеджер контекста `contextlib.closing` для автоматического закрытия
подключения после выполнения операции выборки из базы данных.
"""
import os
import sqlite3, contextlib
con = sqlite3.connect(":memory:")
with contextlib.closing(con):
    print(con.execute("select 1").fetchall())


"""
Перенаправление стандартного вывода и ошибок с помощью `contextlib.redirect_stdout` и `contextlib.redirect_stderr` 
позволяет нам управлять выводом нашего кода, не изменяя сам код. Это особенно полезно, когда мы работаем с кодом 
сторонних библиотек или когда наш код содержит множество операций ввода-вывода.
В случае с `contextlib.redirect_stdout` мы перенаправляем стандартный вывод (обычно это консоль или терминал) в
указанный нами поток. Это может быть файл, поток `sys.stderr` или даже объект `io.StringIO` для сбора вывода в памяти.
Этот метод используется, когда нам нужно сохранить логи или результаты работы программы.
"""
from contextlib import redirect_stdout
import sys
with redirect_stdout(sys.stderr):
    print("Ready to make everybody happy!")


from contextlib import redirect_stderr
with open("error_log.txt", "w") as error_file:
    with redirect_stderr(error_file):
        print("errors!")


"""
попробуем удалить файл "file.txt". Если файла нет на диске, можем просто проигнорировать исключение, если оно возникнет

Однако гораздо удобнее и красивее реализовать это с помощью `contextlib.suppress`
"""

with contextlib.suppress(FileNotFoundError, IOError):
    os.remove("nofile.txt")
