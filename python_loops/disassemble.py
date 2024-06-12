import dis
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
    print(dis.dis(big_outer_loop))
    exit()
