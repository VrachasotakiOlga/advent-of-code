def read_file(file_name: str = "test.txt"):
    positions = dict()
    with open(file_name) as f:
        for col, word in enumerate(f):
            for row, letter in enumerate(word):
                positions[row + 1j * col] = letter

    return positions


def part1(file_name: str) -> int:
    result = 0
    positions = read_file(file_name)

    def g(c: tuple[int, int]) -> str:
        return positions.get(c, "")

    for p in positions:
        if g(p) == "X":
            for d in [1j, -1j, 1, -1, 1 + 1j, -1 - 1j, 1 - 1j, -1 + 1j]:
                result += g(p) + g(p + d) + g(p + d * 2) + g(p + d * 3) == "XMAS"

    return result


def part2(file_name: str) -> int:
    result = 0
    positions = read_file(file_name)

    def g(c: tuple[int, int]) -> str:
        return positions.get(c, "")

    for p in positions:
        if g(p) == "A":
            for d in [1 + 1j, -1 - 1j, 1 - 1j, -1 + 1j]:
                result += (
                    g(p - d) + g(p) + g(p + d) == "MAS"
                    and g(p - d * 1j) + g(p + d * 1j) == "MS"
                )

    return result


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
