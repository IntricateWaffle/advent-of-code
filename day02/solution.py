from pathlib import Path

# puzzle_input = Path("test.txt")
puzzle_input = Path("input.txt")

def translate_move(letter_input: str):
    letter = letter_input.lower()
    print(f"{letter=}")
    if (letter == "a") or (letter == "x"):
        move = "rock"
    elif (letter == "b") or (letter == "y"):
        move = "paper"
    elif (letter == "c") or (letter == "z"):
        move = "scissors" 
    else:
        print("This is not a valid letter")
    print('translated ' f"{move=}")
    return move

def calculate_outcome(opponent, you):
    if opponent == you:
        outcome = "draw"
    elif (you== "rock") and (opponent== "scissors"):
        outcome = "win"
    elif (you== "scissors") and (opponent== "paper"):
        outcome = "win"
    elif (you== "paper") and (opponent== "rock"):
        outcome = "win"
    else:
        outcome = "lose"
    # rock > scissors, 
    # scissors > paper, 
    # paper > rock
    print('calculated ' f"{outcome=}")
    return outcome

# print(determine_outcome("rock", "scissors"))


def calculate_points(outcome, choice):
    # rock = {"score": 1}
    # paper = {"score": 2,}
    # scissors = {"score": 3}
    # Loss = 0
    # Draw = 3
    # Win = 6
    if outcome == "win":
        points = 6
    elif outcome == "draw":
        points = 3
    elif outcome == "lose":
        points = 0
    if choice == "rock":
        points += 1
    elif choice == "paper":
        points += 2
    elif choice == "scissors":
        points += 3
    print('calculated ' f"{points=}")
    return points

# print(calculate_points("win", "rock)"))



total_points = 0
with open(puzzle_input, "r") as f:
    lines = [line.rstrip() for line in f]
    print(lines)
    for line in lines:
        opponent = translate_move(line[0])
        you = translate_move(line[2])
        print(f"{opponent=}")
        print(f"{you=}")
        total_points += calculate_points(calculate_outcome(opponent, you), you)
        print(f"{total_points=}")
    pass



# Rock = ['A', 'X', 1]
# Paper = ['B', 'Y', 2]
# Scissors = ['C', 'Z', 3]






