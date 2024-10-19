import re
from dataclasses import dataclass


def read_file(file_name: str = "input.txt") -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()


@dataclass
class ScratchCard:
    id: int
    winning_numbers: set[int]
    numbers: set[int]

    def num_winning_numbers(self) -> int:
        return len(self.winning_numbers & self.numbers)

    def score(self) -> int:
        x = self.num_winning_numbers()
        return 2 ** (x - 1) if x > 0 else 0


P = r"^Card +(\d+): +(.*) +\| +(.*)"


def parse_scratchcards(scratchcards_raw: list[str]) -> list[ScratchCard]:
    c = re.compile(P)
    lst = []
    for line in scratchcards_raw:
        m = c.match(line)

        if m is None:
            raise ValueError("Xie agapw Oga mou <3")

        id_ = int(m.group(1))
        winning_nums = {int(x) for x in m.group(2).split()}
        nums = {int(x) for x in m.group(3).split()}
        lst.append(ScratchCard(id=id_, winning_numbers=winning_nums, numbers=nums))

    return lst


def part1() -> int:
    scratchcards = parse_scratchcards(read_file())
    return sum(card.score() for card in scratchcards)


def part2() -> int:
    scratchcards = parse_scratchcards(read_file())
    n = len(scratchcards)
    lst = [1] * n
    for i, card in enumerate(scratchcards):
        for j in range(i + 1, i + card.num_winning_numbers() + 1):
            lst[j] += lst[i]

    return sum(lst)


# print(part1())
print(part2())
