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


def is_valid_cubeset(cubeset: tuple[int, int, int]) -> bool:
    final_tuple = (12, 13, 14)
    return (
        cubeset[0] <= final_tuple[0]
        and cubeset[1] <= final_tuple[1]
        and cubeset[2] <= final_tuple[2]
    )


def is_valid_game(cubesets: list[tuple[int, int, int]]) -> bool:
    return all(is_valid_cubeset(cubeset) for cubeset in cubesets)


def part1(file_name) -> int:
    res = 0
    for game_str in read_file(file_name):
        game_id, cubesets = parse_game(game_str)
        if is_valid_game(cubesets):
            res += game_id

    return res


print(part1("input.txt"))
