def read_file(file_name="test.txt") -> list[list[int]]:
    lines = []
    with open(file_name) as f:
        for line in f:
            lines.append(list(map(int, line.split())))
    return lines


def is_increasing(line: list[int]) -> bool:
    return True if line[0] < line[1] else False


def is_safe(line: list[int]) -> bool:
    if is_increasing(line):
        return all(
            line[i] + 1 <= line[i + 1] <= line[i] + 3 for i in range(len(line) - 1)
        )
    else:
        return all(
            line[i] - 1 >= line[i + 1] >= line[i] - 3 for i in range(len(line) - 1)
        )


def tolerate_bad_level(line: list[int]):
    for j in range(len(line)):
        yield [value for (i, value) in enumerate(line) if i != j]


def part1(file_name: str) -> int:
    return sum(is_safe(line) for line in read_file(file_name))


def part2(file_name: str) -> int:
    return sum(
        any(is_safe(e) for e in tolerate_bad_level(line))
        for line in read_file(file_name)
    )


for line in read_file():
    for e in tolerate_bad_level(line):
        print(e)


if __name__ == "__main__":
    print("part1 solution:", part1("input.txt"))
    print("part2 solution:", part2("input.txt"))
