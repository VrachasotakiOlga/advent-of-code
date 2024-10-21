import re
from math import prod


def read_file(file_name: str = "input.txt"):
    with open(file_name) as f:
        return f.read().splitlines()


P = r"\d+"


def parse_line(line: str) -> list[int]:
    c = re.compile(P)
    m = c.findall(line)
    return [int(x) for x in m]


time_lst = parse_line(read_file()[0])
distance_lst = parse_line(read_file()[1])


def ways_to_win(time: int, distance: int) -> int:
    ways_lst = []
    for i in range(1, time):
        if ((time - i) * i) > distance:
            ways_lst.append((time - i) * i)

    return len(ways_lst)


def part1(time_lst, distance_lst):
    return prod(map(ways_to_win, time_lst, distance_lst))


print(part1(time_lst, distance_lst))
