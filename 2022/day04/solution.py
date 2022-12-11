from pathlib import Path


# puzzle_input = Path("test.txt ")
puzzle_input = Path("input.txt")

def get_assignment_range(assignment_input):
    assignment_range = list()
    split_assignment = assignment_input.split('-')
    for i in range(int(split_assignment[0]), int(split_assignment[1])+1):
        assignment_range.append(i)
    print(f"{assignment_range=}")   
    return assignment_range

def get_split_assignmet(assignments_input):
    split_assignments = assignments_input.split(',')
    print(f"{split_assignments=}")
    return split_assignments

def get_assignment_overlap(assignment1: list, assignment2: list):
    set1 = set(assignment1)
    set2 = set(assignment2)
    assignment_overlap = set1 & set2
    print(f"{assignment_overlap=}")
    if assignment_overlap == set1 or assignment_overlap == set2:
        full_overlap = True
    else:
        full_overlap = False
    print(f"{full_overlap=}")
    return full_overlap


def part1(input_lines):
    full_overlaps = 0
    for line in input_lines:
        ranges = list()
        split_assignment = get_split_assignmet(line)
        for assignment in split_assignment:
            ranges.append(get_assignment_range(assignment))
        if get_assignment_overlap(ranges[0], ranges[1]) == True:
            full_overlaps += 1
            print(f"{full_overlaps=}")
    print("part1")
    print(f"{full_overlaps=}")
    return

def main():
    with open(puzzle_input, "r") as f:
        lines = [line.rstrip() for line in f]
        print(f"{lines=}")
    part1(lines)


main()

