type Point = tuple[int, int]
type Grid = list[str]
import sys


def read_file(file_name: str) -> Grid:
    with open(file_name) as f:
        return f.read().splitlines()


def init_pos_and_direction(grid: Grid) -> tuple[Point, Point]:
    num_rows = len(grid)
    num_cols = len(grid[0])
    letters_to_dir = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] in letters_to_dir:
                return (i, j), letters_to_dir[grid[i][j]]

    raise ValueError("Directions not found")


def visited_pos(grid: Grid, init_pos: Point, init_dir: Point) -> set[Point]:
    num_rows = len(grid)
    num_cols = len(grid[0])
    x, y = init_pos
    dx, dy = init_dir

    visited = set()

    while 0 <= x < num_rows and 0 <= y < num_cols:
        if grid[x][y] == "#":
            (x, y) = (x - dx, y - dy)
            (dx, dy) = (dy, -dx)
        else:
            visited.add((x, y))

        (x, y) = (x + dx, y + dy)

    return visited


def can_loop(grid: Grid, obstacle: Point, init_pos: Point, init_dir: Point) -> bool:
    num_rows = len(grid)
    num_cols = len(grid[0])
    x, y = init_pos
    dx, dy = init_dir

    seen = set()

    while 0 <= x < num_rows and 0 <= y < num_cols:
        if (x, y, dx, dy) in seen:
            return True

        if grid[x][y] == "#" or (x, y) == obstacle:
            (x, y) = (x - dx, y - dy)
            (dx, dy) = (dy, -dx)
        else:
            seen.add((x, y, dx, dy))

        (x, y) = (x + dx, y + dy)

    return False


def main():
    file_name = sys.argv[1]
    grid = read_file(file_name)
    init_pos, init_dir = init_pos_and_direction(grid)
    visited = visited_pos(grid, init_pos, init_dir)
    part1 = len(visited)
    part2 = sum(can_loop(grid, obstacle, init_pos, init_dir) for obstacle in visited)
    print(f"part1 is {part1} and part2 is {part2}")


if __name__ == "__main__":
    main()
