class Character:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} Health: {self.health}")

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
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
        return self.name + str(self.health)

        
hero = Character("Hero", 100, 50)
monster = Character("Monster", 100, 50)
monsters = []
print(hero)
hero.cast_spell(30, target=None)

monster.cast_spell(20, target=hero)

hero.heal(10)
