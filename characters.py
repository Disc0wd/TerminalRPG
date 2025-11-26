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

class Hero(Character):
    def __init__(self, name, health, mana, x, y):
        super().__init__(name, health, mana)
        self.x = x 
        self.y = y

    def move(self, dx, dy):
        validDirection = False
        while validDirection != True:
            direction = input("Choose direction (up, down, left, right): ").lower()
            if direction == "up":
                self.y += 1
                print(f"{self.name} moved 1 cell up to {self.x}, {self.y}")
            elif direction == "down":
                self.y -= 1
                print(f"{self.name} moved 1 cell down to {self.x}, {self.y}")
            elif direction == "right":
                self.y += 1
                print(f"{self.name} moved 1 cell right to {self.x}, {self.y}")
            elif direction == "left":
                self.y -= 1
                print(f"{self.name} moved 1 cell left to {self.x}, {self.y}")
            else:
                print("Invalid direction. try again!")
    
    def check_cell(self, prow, pcol):
        pass