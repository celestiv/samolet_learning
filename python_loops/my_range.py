ROWS = 5
COLUMNS = 100
TIMEIT_ITER = 100000


def my_range(limit):
    counter = 0
    while counter < limit:
        yield 1
        counter += 1
    my_range.called += counter


my_range.called = 0

for _ in my_range(COLUMNS):
    for _ in my_range(ROWS):
        pass

print(my_range.called)  # 600

my_range.called = 0

for _ in my_range(ROWS):
    for _ in my_range(COLUMNS):
        pass

print(my_range.called)  # 505
