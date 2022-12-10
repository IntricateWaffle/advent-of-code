from pathlib import Path
import string

puzzle_input = Path("test.txt ")
# puzzle_input = Path("input.txt")


def get_item_type_priority(item_type_letter):
    """
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52
    """
    letters = string.ascii_letters
    item_types = dict()

    for i in range(len(letters)):
        item_types[letters[i]]=i+1
    # print(f"{item_types=}")
    priority = item_types[item_type_letter]
    print(f"{priority=}")
    return priority

def get_groups(sacks, group_size):
    if len(sacks) % group_size == 0:
        print("valid group size")
    else:
        print("invalid group size")
    groups = list()
    print(f"{len(sacks)=}")
    counter = 0
    while counter < len(sacks):
        group = sacks[counter:counter+group_size]
        print(f"{group=}")
        groups.append(group.copy())
        group.clear()
        counter += group_size
    print('get_ 'f"{groups=}")
    return groups

def get_group_assignment(group):
    print('input 'f"{group=}")
    for sack in group:
        if sack is group[-1]:
            break
        for item_type in sack:
            if item_type in sack and sack:
                print("WWWWWWWWWWWWWWWWOWOWOWOWOWOWOWOWOWOWO")
    group_assignment = 0
    print(f"{group_assignment=}")
    return group_assignment


with open(puzzle_input, "r") as f:
    sacks = [line.rstrip() for line in f]
    print(f"{sacks=}")
    groups = get_groups(sacks, 3)
    print(f"{groups=}")
    get_group_assignment(groups)
    import sys;exit()
    sack_priorities = list() 
    for sack in sacks:
        print(f"{sack=}")
        compartment_1 = sack[:len(sack)//2]
        compartment_2 = sack[len(sack)//2:]
        print(f"{compartment_1=}")
        print(f"{compartment_2=}")
        for compartment_item in compartment_1:
            print(f"{compartment_item=}")
            if compartment_item in compartment_2:
                print(f"{compartment_item in compartment_2=}")
                item_priority = get_item_type_priority(compartment_item)
                print(f"{item_priority=}")
                sack_priorities.append(item_priority)
                break
            else:
                print(f"{compartment_item in compartment_2=}")
    print(f"{sack_priorities=}")
    total_priorities = sum(sack_priorities)
    print(f"{total_priorities=}")
    pass