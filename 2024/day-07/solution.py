def read_file(file_name: str) -> list[tuple[int, list[int]]]:
    equations = []

    with open(file_name) as f:
        for line in f:
            exp_str, nums_str = line.split(":", maxsplit=1)
            nums = list(map(int, nums_str.split()))
            equations.append((int(exp_str), nums))

    return equations


def concat(left: int, right: int) -> int:
    t = right
    while t != 0:
        t //= 10
        left *= 10
    return left + right


def is_valid_equation(
    exp: int, nums: list[int], with_concat: bool, evaluated: int, index: int = 1
) -> bool:
    if index == len(nums):
        return exp == evaluated

    if is_valid_equation(exp, nums, with_concat, evaluated + nums[index], index + 1):
        return True

    if is_valid_equation(exp, nums, with_concat, evaluated * nums[index], index + 1):
        return True

    if with_concat and is_valid_equation(
        exp, nums, with_concat, concat(evaluated, nums[index]), index + 1
    ):
        return True

    return False


def main():
    equations = read_file("input.txt")
    part_1 = sum(
        exp
        for exp, nums in equations
        if is_valid_equation(exp, nums, False, nums[0], 1)
    )
    part_2 = sum(
        exp for exp, nums in equations if is_valid_equation(exp, nums, True, nums[0], 1)
    )
    print(part_1)
    print(part_2)


if __name__ == "__main__":
    main()
