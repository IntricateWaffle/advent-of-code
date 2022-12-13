from pathlib import Path


# puzzle_input = Path("test.txt ")
puzzle_input = Path("input.txt")

def get_sop_marker(input_line):
    print(f"{input_line=}")
    for i in range(len(input_line)):
        possible_sop_marker = set(input_line[i:i+4])
        print(f"{possible_sop_marker=}")
        if len(possible_sop_marker) == 4:
            print(f"{i+4=}")
            break
        

    print(f"{possible_sop_marker=}")
    return

def part1(input_lines):
    for line in input_lines:
        get_sop_marker(line)
    return

def main():
    with open(puzzle_input, "r") as f:
        lines = [line.strip() for line in f]
        print(f"{lines=}")
    part1(lines)
main()