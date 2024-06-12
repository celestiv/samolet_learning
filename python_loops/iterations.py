import random
import timeit

ROWS = 5
COLUMNS = 100
TIMEIT_ITER = 100000

table = tuple(
    tuple(
        random.randint(1000, 10000)
        for _ in range(COLUMNS)
    )
    for _ in range(ROWS)
)


def big_outer_loop():
    iterations = overall_sum = 0
    for column in range(COLUMNS):
        iterations += 1
        for row in range(ROWS):
            iterations += 1
            overall_sum += table[row][column]
    print(f"{overall_sum=}, {iterations=}")


def small_outer_loop():
    iterations = overall_sum = 0
    for row in range(ROWS):
        iterations += 1
        for column in range(COLUMNS):
            iterations += 1
            overall_sum += table[row][column]
    print(f"{overall_sum=}, {iterations=}")


def main():
    big_outer_loop()
    small_outer_loop()


if __name__ == "__main__":
    main()
