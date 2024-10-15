import operator
import re
from functools import reduce

file_name = "input.txt"


def read_file(file_name=file_name):
    with open(file_name) as f:
        return f.read().splitlines()


P = re.compile(r"\d+")
P1 = re.compile(r"[*]")


def chars_positions(file_name: str = file_name):
    lines = read_file(file_name)
    gear = dict()  # type ignore
    for i, line in enumerate(lines):
        for m in re.finditer(P1, line):
            gear[(i, m.start())] = []

    return gear


def digits_positions(file_name=file_name):
    lines = read_file(file_name)
    chars_lst = chars_positions(file_name)
    for i, line in enumerate(lines):
        for m in re.finditer(P, line):
            for a in range(i - 1, i + 2):
                for b in range(m.start() - 1, m.end() + 1):
                    if (a, b) in chars_lst:
                        chars_lst[(a, b)].append(int(m.group()))

    return chars_lst


def multiply_list_items(lst):
    return reduce(operator.mul, lst)


def part2(file_name):
    res = 0
    for key, value in digits_positions(file_name).items():
        if len(value) == 2:
            res += multiply_list_items(value)
    return res


print(part2(file_name))
