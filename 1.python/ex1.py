people = [
    {"name": "Vasya", "age": 14},
    {"name": "Petya", "age": 15},
    {"name": "Masha", "age": 13}
]

sorting_func = lambda k: sorted(k["age"] for k in people)

if __name__ == "__main__":
    people.sort(key=lambda person: person["age"])
    print(*[p for p in people], sep="\n")
