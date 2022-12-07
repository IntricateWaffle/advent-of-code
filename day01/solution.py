from pathlib import Path

# puzzle_input = Path("./day01/test")
puzzle_input = Path("./day01/input")


with open(puzzle_input, "r") as f:
    lines = [line.rstrip() for line in f]
    print(lines)
    totals = []
    total = 0
    for i in lines:
        print(f"{totals=}")
        if i.isdigit() == True:
            print(f"{i=}")
            total += int(i)
            print(f"{total=}")
            if i is lines[-1]:
                totals.append(total)
        elif i.isdigit() == False:
            print(f"{totals=}")
            print(f"{totals=}")
            totals.append(total)
            total = 0
    totals.sort()
    print(f"{totals=}")
    print(f"{totals[-1]=}")
    top_three_total = totals[-1] + totals[-2] + totals[-3]
    print(f"{top_three_total=}")
