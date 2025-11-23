import random

class Character:
    def __init__(self, name, health, mana):
        self.name = name
        self.max_health = health
        self.health = health
        self.mana = mana
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} Health: {self.health}")

    def heal(self, amount):
        self.health += amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        elif self.health < 0:
            self.health = 0
        else:
            pass
        print(f"{self.name} uses a heal potion!")
        print(f"{self.name} Health: {self.health}")

    def cast_spell(self, cost, target=None):
        if self.mana >= cost:
            self.mana -= cost
            print(f"{self.name} casts a spell! Mana left: {self.mana}")
            if target:
                target.take_damage(cost)
        else:
            print(f"{self.name} does not have enough mana!")

    def __str__(self):
        return self.name + "\nHealth: " + str(self.health) + "\n\n"

        
hero = Character("Hero", 100, 50)
monster = Character("Monster", 100, 50)

enemies = [Character("Monster" + str(i), random.randint(80, 120), random.randint(25, 60)) for i in range(5)]

for enemy in enemies:
    print(enemy)

choice = input("Which monster do you want to target? ")
target = None

for enemy in enemies:
    if enemy.name == choice:
        target = enemy

if target is not None:
    hero.cast_spell(30, target)
    target.cast_spell(30, hero)


# 6x6 grid
grid = [
    [
        Character(f"Monster {col}{row}", random.randint(80, 120), random.randint(25, 60))
        if random.randint(0, 20) > 17
        else None
        for col in range(6)
    ]
    for row in range(10)
]

# print the grid
layout = "{:^16}{:^16}{:^16}{:^16}{:^16}{:^16}"

for row in grid:
    output = []
    for item in row:
        if isinstance(item, Character):
            output.append(f"{item.name}")   # show monster name
        else:
            output.append("[===== . =====]")       # empty cell symbol

    print(layout.format(*output))

