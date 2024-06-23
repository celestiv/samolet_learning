import sqlite3
from typing import Optional, Type
from types import TracebackType


class SQLite3CM:
    """
    Метод `__enter__`. Здесь мы устанавливаем соединение с базой данных и возвращаем курсор.
        Это позволяет выполнять SQL-запросы внутри блока `with`.
    Метод `__exit__`. Этот метод вызывается по завершении блока `with`. Здесь мы выполняем `commit`,
        чтобы сохранить изменения, сделанные в БД, и закрываем соединение с БД. Можно также добавить обработку исключений
        для обеспечения более надежной работы.
    """
    def __init__(self, path):
        self.path = path
        self.conn = None

    def __enter__(self) -> sqlite3.Cursor:
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ):
        self.conn.commit()
        self.conn.close()


with SQLite3CM("example.db") as c:
    c.execute("create table t(x int)")
    c.execute("insert into t values (1), (2)")

with SQLite3CM("example.db") as c:
    assert c.execute("select count(*) from t").fetchone() == (2, )  # no error
