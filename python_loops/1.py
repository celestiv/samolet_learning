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
    overall_sum = 0
    for column in range(COLUMNS):
        for row in range(ROWS):
            overall_sum += table[row][column]


def small_outer_loop():
    overall_sum = 0
    for row in range(ROWS):
        for column in range(COLUMNS):
            overall_sum += table[row][column]


def with_sum():
    return sum(sum(column for column in row) for row in table)


def main():
    big_outer_loop_time = round(timeit.timeit(big_outer_loop, number=TIMEIT_ITER), 2)
    small_outer_loop_time = round(timeit.timeit(small_outer_loop, number=TIMEIT_ITER), 2)
    with_sum_time = round(timeit.timeit(with_sum, number=TIMEIT_ITER), 2)
    print(f"{big_outer_loop_time=}, {small_outer_loop_time=}, {with_sum_time=}")

    delta = round(100*(big_outer_loop_time - small_outer_loop_time) / big_outer_loop_time)
    delta2 = round(100*(big_outer_loop_time - with_sum_time) / big_outer_loop_time)
    print(f"{delta=}, {delta2=}")


if __name__ == "__main__":
    main()
