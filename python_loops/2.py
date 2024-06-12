import timeit

ROWS = 5
COLUMNS = 100
TIMEIT_ITER = 100000


def big_outer_loop():
    overall_sum = 0
    for column in range(COLUMNS):
        for row in range(ROWS):
            overall_sum += 1


def small_outer_loop():
    overall_sum = 0
    for row in range(ROWS):
        for column in range(COLUMNS):
            overall_sum += 1


def main():
    big_outer_loop_time = round(timeit.timeit(big_outer_loop, number=TIMEIT_ITER), 2)
    small_outer_loop_time = round(timeit.timeit(small_outer_loop, number=TIMEIT_ITER), 2)
    print(f"{big_outer_loop_time=}, {small_outer_loop_time=}")
    delta = round(100*(big_outer_loop_time - small_outer_loop_time) / big_outer_loop_time)

    print(f"{delta=}")


if __name__ == "__main__":
    main()
