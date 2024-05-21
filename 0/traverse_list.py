def recursive_traverse(item_list):
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += recursive_traverse(item_list=item)
        else:
            count += 1
    return count


def stack_traverse(item_list):
    current_list = item_list
    count = 0
    stack = []
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue
        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1



if __name__ == "__main__":
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    # print(recursive_traverse(names))
    print(stack_traverse(names))