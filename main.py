from characters import Character
from grid import generate_grid, print_grid
import random

hero = Character("Hero", 100, 50)
enemies = [Character("Monster" + str(i), random.randint(80, 120), random.randint(25, 60)) for i in range(5)]

for enemy in enemies:
    print(enemy)

choice = input("Which monster do you want to target? ")

target = next((e for e in enemies if e.name == choice), None)

if target:
    hero.cast_spell(30, target)
    target.cast_spell(30, hero)

# create grid
grid = generate_grid()
print_grid(grid)
