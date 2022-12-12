from pathlib import Path


puzzle_input = Path("test.txt ")
# puzzle_input = Path("input.txt")

def get_crates(input_lines):
    crates = list()
    crates_dict = {}
    for line in input_lines:
        print(f"{line=}")
        if "1" in line:
            print("stack numbers: "f'{line=}')
            print(input_lines.index(line))
            for num in line:
                if num.isdigit() == True:
                    crates_dict[num] = list()
                    print(f"{crates_dict=}")
                break
        else:
            crates.append(line)
        for row in crates:
            print(f"{row=}")
            for crate in row:
                print(f"{crate=}")
        if line == '':
            print("blank")
            break
        print(f"{crates=}")
    return

def get_planned_steps():
    return

def part1(input_lines):
    get_crates(input_lines)
    return

def main():
    with open(puzzle_input, "r") as f:
        lines = [line.strip('\n') for line in f]
        print(f"{lines=}")
    part1(lines)
main()