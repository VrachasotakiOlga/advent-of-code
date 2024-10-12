import re
import sys
from collections.abc import Generator


def read_file(file_name="test.txt") -> Generator[str, None, None]:
    with open(file_name, "r") as f:
        for line in f:
            yield line.rstrip("\n")


P1 = re.compile(r"\D*(\d).*(\d)\D*$")
P2 = re.compile(r".*?(\d)")


def find_edge_digits(string: str) -> int:
    m1 = P1.match(string)
    if m1 is None:
        m2 = P2.search(string)
        if m2 is None:
            raise ValueError("Invalid match")
        return int(m2.group(1) + m2.group(1))
    return int(m1.group(1) + m1.group(2))


res = sum(map(find_edge_digits, read_file(sys.argv[1])))
print(res)
