import random
from characters import Character

def generate_grid():
    grid = [
        [
            Character(f"Monster {col}{row}", random.randint(80, 120), random.randint(25, 60))
            if random.randint(0, 20) > 17
            else None
            for col in range(6)
        ]
        for row in range(10)
    ]
    return grid


def print_grid(grid):
    layout = "{:^16}{:^16}{:^16}{:^16}{:^16}{:^16}"

    for row in grid:
        output = []
        for item in row:
            if isinstance(item, Character):
                output.append(f"[  {item.name} ]")
            else:
                output.append("[===== . =====]")
        print(layout.format(*output))
