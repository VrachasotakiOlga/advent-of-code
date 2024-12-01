from collections import Counter


def read_file(file_name="test.txt") -> tuple[list[int], list[int]]:
    left = []
    right = []
    with open(file_name) as f:
        for line in f:
            x, y = map(int, line.split(maxsplit=1))
            left.append(x)
            right.append(y)

    return left, right


def total_distance(left: list[int], right: list[int]) -> int:
    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


def similarity_score(left: list[int], right: list[int]) -> int:
    c = Counter(right)
    return sum(x * c.get(x, 0) for x in left)


def main():
    left, right = read_file("input.txt")
    part1 = total_distance(left, right)
    part2 = similarity_score(left, right)
    print(part1, part2)


if __name__ == "__main__":
    main()
