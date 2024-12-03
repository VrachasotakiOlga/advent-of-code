import math
import re


def read_file(file_name: str = "test.txt") -> str:
    with open(file_name) as f:
        return f.read()


p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def delete_disabled_muls(memory: str) -> str:
    return re.sub(r"don't\(\).*?do\(\)", "", memory, flags=re.DOTALL)


def valid_mul_in_line(memory: str) -> list[list[int]]:
    m = p.findall(memory)
    return [list(map(int, i)) for i in m]


def part1(file_name: str) -> int:
    memory = read_file(file_name)
    return sum(math.prod(i) for i in valid_mul_in_line(memory))


def part2(file_name: str) -> int:
    memory = read_file(file_name)
    new_memory = delete_disabled_muls(memory)
    return sum(math.prod(i) for i in valid_mul_in_line(new_memory))


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
