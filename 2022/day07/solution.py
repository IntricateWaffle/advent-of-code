from pathlib import Path


puzzle_input = Path("test.txt ")
# puzzle_input = Path("input.txt")

def part1(input_lines):
    for line in input_lines:
        print(line)
        pass
    return

def part2(input_lines):
    for line in input_lines:
        pass
    return


def main():
    with open(puzzle_input, "r") as f:
        lines = [line.strip() for line in f]
        print(f"{lines=}")
    part1(lines)
    # part2(lines)
main()