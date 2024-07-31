import re


def validate_email(email: str) -> bool:
    """
        xxx.x.xx@sberbank.ru   
    """
    regex = re.compile(r"^[a-zA-Z0-9]{1-3}+\.{0,1}[a-zA-Z0-9]{1}+\.{0,1}[a-zA-Z0-9]{1-2}@sberbank\.ru$")
    return re.match(regex, email) is not None


def main():
    valid_email = 0
    while valid_email != 1:
        email = input()
        valid_email = int(validate_email(email=email))
        if valid_email:
            print("Успех!")
        else:
            print("Неподходящий")



if __name__ == "__main__":
    main()
