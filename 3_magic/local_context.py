"""
В некоторых случаях, например в финансовых расчетах или научных вычислениях, требуется большая точность.
 Python позволяет управлять точностью вычислений с помощью модуля `decimal`. Для временного изменения точности
 вычислений используется контекстный менеджер `decimal.localcontext`.
"""
import decimal

for i in range(100, -1, -1):
    if 1 + 2 ** (-i) > 1:
        print(f"Accuracy float: {i}")  # обычно выводит 52
        break


with decimal.localcontext() as ctx:
    ctx.prec = 30  # устанавливаем точность до 30 знаков
    one = decimal.Decimal(1)
    two = decimal.Decimal(2)
    for i in range(100, -1, -1):
        if ctx.add(one, ctx.power(two, decimal.Decimal(-i))) > one:
            print(f"Accuracy decimal: {i}")  # обычно больше чем 52, например 97
            break
