import sys


def read_file(file_name: str) -> tuple[set[tuple[int, int]], list[list[int]]]:
    with open(file_name) as f:
        rules_str, manuals_str = f.read().split("\n\n", maxsplit=1)

    rules = set()
    for rule in rules_str.splitlines():
        left, right = rule.split("|", maxsplit=1)
        rules.add((int(left), int(right)))

    manuals = []
    for manual in manuals_str.splitlines():
        m = list(map(int, manual.split(",")))
        manuals.append(m)

    return rules, manuals


def is_ordered_manual(manual: list[int], rules: set[tuple[int, int]]) -> bool:
    return all((manual[i], manual[i + 1]) in rules for i in range(len(manual) - 1))


def middle_manual_page(manual: list[int]) -> int:
    return manual[len(manual) // 2]


def bubble_sort(manual: list[int], rules: set[tuple[int, int]]) -> list[int]:
    n = len(manual)
    while True:
        swapped = False
        for i in range(1, n):
            if (manual[i - 1], manual[i]) not in rules:
                swapped = True
                manual[i - 1], manual[i] = manual[i], manual[i - 1]
        n -= 1
        if not swapped:
            return manual


def solution(file_name: str):
    part1 = 0
    part2 = 0
    rules, manuals = read_file(file_name)
    for manual in manuals:
        if is_ordered_manual(manual, rules):
            part1 += middle_manual_page(manual)
        else:
            sorted_manual = bubble_sort(manual, rules)
            part2 += middle_manual_page(sorted_manual)

    return part1, part2


if __name__ == "__main__":
    file_name = sys.argv[1]
    print(solution(file_name))
