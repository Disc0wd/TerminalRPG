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
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health < 0:
            self.health = 0
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
        return f"{self.name}\nHealth: {self.health}\n"
