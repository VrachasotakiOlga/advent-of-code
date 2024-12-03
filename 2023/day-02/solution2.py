import re


def read_file(file_name="test.txt") -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()


def parse_game_id(line: str) -> int:
    p = re.compile(r"^Game (\d+)")
    m = p.match(line)
    if m is None:
        raise ValueError("No match")

    return int(m.group(1))


# 3 blue, 4 red
def parse_cubeset(string: str) -> tuple[int, int, int]:
    res = [0, 0, 0]
    for x in string.split(", "):
        num_str, color = x.split(" ", 1)
        num = int(num_str)
        match color:
            case "red":
                res[0] = num
            case "green":
                res[1] = num
            case "blue":
                res[2] = num
            case _:
                raise ValueError("No match")

    assert len(res) == 3
    return tuple(res)  # type: ignore


def parse_game(line: str):
    game_str, cubesets_str = line.split(": ", 1)
    game_id = parse_game_id(game_str)
    cubesets = [parse_cubeset(x) for x in cubesets_str.split("; ")]
    return game_id, cubesets


def minimum_cubeset(cubesets: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    min_lst = [0, 0, 0]
    for cubeset in cubesets:
        if cubeset[0] > min_lst[0]:
            min_lst[0] = cubeset[0]
        if cubeset[1] > min_lst[1]:
            min_lst[1] = cubeset[1]
        if cubeset[2] > min_lst[2]:
            min_lst[2] = cubeset[2]

    return tuple(min_lst)  # type:ignore


def part2(file_name) -> int:
    res = 0
    for game_str in read_file(file_name):
        _, cubesets = parse_game(game_str)
        r, g, b = minimum_cubeset(cubesets)
        res += r * g * b

    return res


# print(part2("test.txt"))

print(part2("input.txt"))
