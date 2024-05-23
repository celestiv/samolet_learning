class A:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"{__class__.__name__}({self.x})"


def main():
    a = A(42)
    print(a)


if __name__ == "__main__":
    main()
