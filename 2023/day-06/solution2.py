import re


def read_file(file_name: str = "input.txt"):
    with open(file_name) as f:
        return f.read().splitlines()


P = r"\d+"


def parse_line(line: str) -> int:
    c = re.compile(P)
    m = c.findall(line)
    return int("".join(m))


time = parse_line(read_file()[0])
distance = parse_line(read_file()[1])


def ways_to_win(time: int, distance: int) -> int:
    ways_lst = []
    for i in range(1, time):
        if ((time - i) * i) > distance:
            ways_lst.append((time - i) * i)

    return len(ways_lst)


print(ways_to_win(time, distance))
