from pathlib import Path


puzzle_input = Path("test.txt ")
# puzzle_input = Path("input.txt")

def get_crates(input_lines):
    crates = list()
    crates_dict = {}
    for line in input_lines:
        print(f"{line=}")
        print(f"{len(line)=}")
        crates.append(line)
        if "1" in line:
            for num in line:
                if num.isdigit() == True:
                    crates_dict[num] = list()
                    print(f"{crates_dict=}")
            crates.remove(line)
            break
        for i in range(1, len(crates), 4):
            print(f"{crates[i]=}")

        if line == '':
            print("blank")
            break
        print(f"{crates=}")
    print(f"{crates_dict.keys()=}")

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