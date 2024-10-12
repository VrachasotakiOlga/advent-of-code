import re
import sys
from collections.abc import Generator


def read_file(file_name="test2.txt") -> Generator[str, None, None]:
    with open(file_name, "r") as f:
        for line in f:
            yield line.rstrip("\n")


WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
word_to_num = {word: str(i) for i, word in enumerate(WORDS, 1)}
sub_pattern = r"\d|" + "|".join(WORDS)

P1 = re.compile(rf".*?({sub_pattern}).*({sub_pattern}).*?$")
P2 = re.compile(rf".*?({sub_pattern})")


def translate(string: str) -> str:
    if string in word_to_num:
        return word_to_num[string]
    return string


def find_edge_digits(string: str) -> int:
    m1 = P1.match(string)
    if m1 is None:
        m2 = P2.search(string)
        if m2 is None:
            raise ValueError("Invalid match")
        return int(translate(m2.group(1)) + translate(m2.group(1)))
    return int(translate(m1.group(1)) + translate(m1.group(2)))


res = sum(map(find_edge_digits, read_file(sys.argv[1])))
print(res)
