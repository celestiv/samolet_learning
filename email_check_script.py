
import re

def check_email():
    while True:
        email = input("Введите email: ")
        if not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            print("Некорректный ввод. Пожалуйста, введите правильный email-адрес.")
        elif not re.fullmatch(r"[\w.]+@[\w.]+\.sberbank\.ru", email):
            print("Неподходящий")
        else:
            print("Успех")
            break

if __name__ == "__main__":
    check_email()
