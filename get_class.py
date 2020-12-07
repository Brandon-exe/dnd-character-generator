import random

# randomly choose a class
def get_class():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    char_class = random.choice(classes)
    return char_class