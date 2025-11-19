import random
import time

# Actions, XP, etc.
actions_list = ["fight", "mine", "cut", "craft", "help", "level", "stats", "heal"]
level_a = 0
xp_level = 0
hp = 10
death = 0
completion = 0
request = None
endless = 0
dabloons = 0
cheat_attempts = 0

# Encounters, Ores, Trees
encounters = ["Bat", "Wolf", "Gremlin", "Fantom", "The Undead"]
encounters_int = 0
accept = None 

ores = ["Micro", "Small", "Medium", "Big", "Large"]
ores_int = 0

trees = ["Micro", "Small", "Medium", "Big", "Large"]
trees_int = 0

# Sword Properties
sword_durability = 10
sword_strength = 2
sword_type = 1


# Axe Properties
axe_strength = 2
axe_type = 1

# Pickaxexe Properties
pickaxe_strength = 2
pickaxe_type = 1

# Resources
wood = 1
metal = 2
special_items = 0
health_potion = 0


nickname = input("Welcome Adventurer, what's your name?: ")
print(f'''Welcome to the TerminalRPG adventure {nickname}, 
Here you'll have to increase your level and improve your gear to face the final boss''')

def stats():
    
    level()
    print(f"HP: {hp}")
    print(f"Dabloons: {dabloons}")
    print()
    print(f"Sword Strength: {sword_strength}")
    print(f"Sword Multiplier: {sword_type}")
    print(f"Sword Durability: {sword_durability}")
    print(f"Pickaxe Strength: {pickaxe_strength}")
    print(f"Pickaxe Multiplier: {pickaxe_type}")
    print(f"Axe Strength: {axe_strength}")
    print(f"Axe Multiplier: {axe_type}")
    print()
    print(f"Wood: {wood}")
    print(f"Metal: {metal}")
    print(f"Special Items: {special_items}")
    print(f"Health Potions: {health_potion}")
    print("-" * 30)
    print(" ")

def help():

    global request
    print("-" * 30)

    print("These are all actions(not all actions have explenaitions since they are self explanatory: )", actions_list)
    request = input("What do you need help with?: ")
    print("-" * 30)
    if request == "fight":
        print('''   fight - an action that includes 5 encounters; Bat, Wolf, Gremlin, Phantom and The Undead. 
In accordance with order you'll need 0, 1, 2, 3, 4 strength and durability points to defeat an encounter.
If durability of your sword falls below 0, you won't be able to defeat any enemy, therefore making fighting
useless. To fight certain oponents you'll need to get strength points in 'craft' or 'shop'. If you fight
without having enough strength you'll lose durability and hp.
Possible Loot:'Special Items', 'Health Potions'. ''')
    elif request == "mine" or "cut":
        print(f'''  {request} - action that includes 5 size types of objects; Micro, Small, Medium, Big and Large. 
In accordance with order you'll need 0, 1, 2, 3, 4 strength points on your tool to get the resources.
If you don't have enough strength, you wont be able to get the loot. You can get strenght points with 'craft' or in 'shop'.''')
    elif request == "craft":
        print('''craft - a place where you can get Tool Multipliers and sword repair. 
To execute commands type codes in square brackets: sr, sm, pm, am''')
    elif request == "heal":
        print("You have to have 7 or less HP and 1 Health Potion to heal")
    else:
        print("Obvious Action or Invalid request")

    print("-" * 30)

def fight():

    global sword_strength, sword_type, sword_durability, encounters, encounters_int, hp, health_potion, special_items, xp_level, dabloons

    encounters_int = random.randint(0, 4)
    print("-" * 30)
    print(f"Your next encounter is: {encounters[encounters_int]}, would you like to proceed?: ")
    accept = input("Yes/no: ")
    print("-" * 30)
    if accept == "yes":
        if sword_durability > 0:
            if sword_strength >= encounters_int:
                sword_durability = sword_durability - encounters_int
                health_potion = health_potion + ((encounters_int / 4) * sword_type)
                special_items = special_items + ((encounters_int / 5) * sword_type)
                xp_level = xp_level + (encounters_int * 2)
                dabloons = dabloons + (encounters_int / 2)
                print(f"Fight was succesful, your sword is at {sword_durability} durability points. You gained {encounters_int * 2} XP.")
                print(f"Loot: {encounters_int / 2} - 'Dabloons', {encounters_int / 4} - 'Health Potions', {encounters_int / 5} - 'Special Items'")

            else:
                print("Ouch! this was tough")
                sword_durability = sword_durability - encounters_int
                hp = hp - encounters_int
                print(f'''Your sword is at {sword_durability} durability points and you've lost {encounters_int/2} health. Should be more careful next time''')
        else:
            print("Your sword is broken. Repair it in 'craft'")
    else:
        print("OK! Pacifism is also a way")
    print("-" * 30)

def mine():

    global ores, ores_int, accept, pickaxe_strength, pickaxe_type, metal, xp_level, dabloons
    
    print("-" * 30)

    ores_int = random.randint(0, 4)
    print(f"Your next ore is {ores[ores_int]} Size. Would you like to mine it?")
    accept = input("Yes/no?: ")
    print("-" * 30)
    if accept == "yes":
        if pickaxe_strength >= ores_int:
            metal = metal + ((ores_int + 1) * pickaxe_type)
            xp_level = xp_level + (ores_int + 1)
            dabloons = dabloons + (ores_int / 4)
            print(f"Congrats! You've gained {ores_int + 1} XP!")
            print(f"Loot: {ores_int / 4} - 'Dabloons', {(ores_int + 1)*pickaxe_type} - 'Metal'")
        else:
            print("Your pickaxe is too weak")  
    else:
        print("OK!")
    print("-" * 30)
    print(" ")
    
def cut():

    global trees, trees_int, accept, axe_strength, axe_type, wood, xp_level, dabloons
    
    print("-" * 30)

    trees_int = random.randint(0, 4)
    print(f"Your next tree is {trees[trees_int]} Size. Would you like to cut it down?")
    accept = input("Yes/no?: ")
    print("-" * 30)
    if accept == "yes":
        if axe_strength >= trees_int:
            wood = wood + ((trees_int + 1) * axe_type)
            xp_level = xp_level + (trees_int + 1)
            dabloons = dabloons + (trees_int / 4)
            print(f"Congrats! You've gained {trees_int + 1} XP!")
            print(f"Loot: {trees_int / 4} - 'Dabloons', {(trees_int + 1) * axe_type} - 'Wood'")
        else:
            print("Your axe is too weak")  
    else:
        print("OK!")
    print("-" * 30)
    print(" ")

def craft():

    global request, sword_durability, sword_strength, sword_type, axe_strength, axe_type, pickaxe_strength, pickaxe_type, metal, wood, special_items, accept
    print("-" * 30)
    print("You can craft/repair: Sword Repair[sr], Sword Multipliers[sm], Axe Multipliers[am] and Pickaxe Multipliers[pm]")
    request = input("What do you want to craft?: ")
    print("-" * 30)
    if request == "sm":
        print("You'll need: 2 x 'Metal', 0.4 x 'Special Items'. Would you like to proceed?")
        accept = input("Yes/no?: ")
        if accept == "yes":
            if metal >= 2:
                if special_items >= 0.4:
                    sword_type = sword_type + 0.2
                    sword_strength = sword_strength + 0.5
                    print(f"Your sword multiplier is {sword_type}x, and strength is {sword_strength}")
                else:
                    print("Not enough items!")
            else:
                print("Not enough items!")
        elif accept == "no":
            print("OK!")
        else:
            pass
    elif request == "am":
        print("You'll need: 1 x 'Metal', 0.2 x 'Special Items'. Would you like to proceed?")
        accept = input("Yes/no?: ")
        if accept == "yes":
            if metal >= 1:
                if special_items >= 0.2:
                    axe_type = axe_type + 0.2
                    axe_strength = axe_strength + 0.4
                    print(f"Your sword multiplier is {axe_type}x, and strength is {axe_strength}")
                else:
                    print("Not enough items!")
            else:
                print("Not enough items!")
        elif accept == "no":
            print("OK!")
        else:
            pass
    elif request == "pm":
        print("You'll need: 5 x 'Metal', 0.5 x 'Special Items'. Would you like to proceed?")
        accept = input("Yes/no?: ")
        if accept == "yes":
            if metal >= 5:
                if special_items >= 0.5:
                    pickaxe_type = pickaxe_type + 0.1
                    pickaxe_strength = pickaxe_strength + 0.5
                    print(f"Your sword multiplier is {axe_type}x, and strength is {axe_strength}")
                else:
                    print("Not enough items!")
            else:
                print("Not enough items!")
        elif accept == "no":
            print("OK!")
        else:
            pass
    elif request == "sr":
        print('''You'll need: 4 x 'Metal', 3 x 'Wood' to repair. Would you like to proceed?''')
        accept = input("Yes/no?: ")
        if accept == "yes":
            if metal >= 4:
                if wood >= 3:
                    sword_durability = sword_durability + 3
                    print(f"Your sword was repaired and is at {sword_durability} durability points!")
                else:
                    print("Not enough items!")
            else:
                print("Not enough items!")
        elif accept == "no":
            print("OK!")
        else:
            pass
    else:
        print("Invalid request")
    print("-" * 30)

def level():

    global xp_level, level_a
    
    print("-" * 30)
    if xp_level < 20:
        print(f"Level 1: {xp_level}/20XP")
        level_a = 1
    elif xp_level < 50:
        print(f"Level 2: {xp_level}/50XP")
        level_a = 2
    elif xp_level < 100:
        print(f"Level 3: {xp_level}/100XP")
        level_a = 3
    elif xp_level < 200:
        print(f"Level 4: {xp_level}/200XP")
        level_a = 4
    else:
        print(f"Level 5: {xp_level}XP")
        level_a = 5
    print("-" * 30)

def heal():

    global accept, health_potion, hp
    print("-" * 30)
    print("You'll need 1 - 'Health Potion' to restore 3 health points. Would you like to proceed?")
    accept = input("Yes/no?: ")
    print("-" * 30)
    if accept == "yes":
        if hp <= 7:
            if health_potion >= 1:
                health_potion = health_potion - 1
                hp = hp +3
                print("3HP restored successfully!")
            else:
                print("Not enough potions")
        else:
            print("Too much health!")
    print("-" * 30)

def shop():

    global dabloons, special_items, health_potion, request
    print("-" * 30)
    print("Welcome to the \"Shop\"")
    time.sleep(1)
    print()
    print("Here's our selection: ")
    time.sleep(0.5)
    print("0 | Health Potions x 1: 30 Dabloons ")
    time.sleep(0.2)
    print("1 | Special items x 3: 15 Dabloons ")
    time.sleep(0.2)
    print("-" * 30)
    request = int(input("Enter item code: "))
    if request == 0:
        if dabloons >= 30:
            dabloons = dabloons - 30
            health_potion = health_potion + 1
            print("1 x 'Health Potion' has been added to your inventory!")
        else:
            print("Not enough dabloons!")
    elif request == 1:
        if dabloons >= 15:
            dabloons = dabloons - 15
            special_items = special_items + 1
            print("1 x 'Special Item' has been added to your inventory!")
        else:
            print("Not enough dabloons!")
    else:
        print("Invalid Item Code")

def cheat():

    global sword_type, sword_strength, pickaxe_type, pickaxe_strength, axe_type, axe_strength, xp_level

    sword_type = 3
    sword_strength = 5
    pickaxe_type = 3
    pickaxe_strength = 5
    axe_type = 3
    axe_strength = 5
    xp_level = 199

while completion == 0:

    if hp > 0:
        action = input("What would you like to do: ")
        
        if level_a == 5:
            if sword_type >= 3 and axe_type >= 3 and pickaxe_type >= 3:
                completion = 1
            else:
                pass
        elif action == "help":
            help()
        elif action == "fight":
            fight()
        elif action == "mine":
            mine()
        elif action == "cut":
            cut()
        elif action == "craft":
            craft()
        elif action == "level":
            level()
        elif action == "stats":
            stats()
        elif action == "heal":
            heal()
        elif action == "shop":
            shop()
        elif action == "cheat":
            if cheat_attempts < 5:
                print("No cheating!")
                cheat_attempts = cheat_attempts + 1
            else:
                print("Alright, let it be your way")
                cheat()

        else:
            print("Invalid action")
    else:
        print("Game Over")
        break

print(f"{nickname}: Ah... the memories")
time.sleep(1)
print("Console: You've had an amnesia, your past life is gone")
time.sleep(2)
print(f"{nickname}: Huh?")
time.sleep(1)
print(f"Console: it's just you and me now, forever, in an endless loop")
time.sleep(2)
print("-" * 30)
endless = input("Press any key + ENTER to continue... ")

while completion == 1:
    if hp > 0:
        action = input("What would you like to do: ")
        if action == "help":
            help()
        elif action == "fight":
            fight()
        elif action == "mine":
            mine()
        elif action == "cut":
            cut()
        elif action == "craft":
            craft()
        elif action == "level":
            level()
        elif action == "stats":
            stats()
        elif action == "heal":
            heal()
        elif action == "shop":
            shop()
        else:
            print("Invalid action")
    else:
        print("Game Over")
        break


