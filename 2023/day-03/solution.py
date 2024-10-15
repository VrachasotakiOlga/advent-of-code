import re

file_name = "input.txt"


def read_file(file_name=file_name):
    with open(file_name) as f:
        return f.read().splitlines()


P = re.compile(r"\d+")
P1 = re.compile(r"[^.\d]")


def chars_positions(file_name: str = file_name):
    lines = read_file(file_name)
    chars_set = set()
    for i, line in enumerate(lines):
        for m in re.finditer(P1, line):
            j = m.start()
            chars_set |= {
                (x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
            }
    return chars_set


chars_lst = chars_positions(file_name)


def digits_positions(file_name=file_name):
    lines = read_file(file_name)
    num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(P, line):
            if any((i, j) in chars_lst for j in range(*m.span())):
                num_sum += int(m.group())

    return num_sum


print(digits_positions(file_name=file_name))
