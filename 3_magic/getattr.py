class A:
    pass


a = A()
setattr(a, "9", "nine")
assert getattr(a, "9") == "nine"  # no error


attr_name = input("Введите значение: ")
default_value = "default value"
value = getattr(a, attr_name, default_value)
print(f"{attr_name}: {value}")  # Если ввести 9 - получаем "nine", иначе "default value"
