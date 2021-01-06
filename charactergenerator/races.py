import random
from . import tables

class Race:
    def __init__(self):
        self. = 
        self.languages = set()
        self.skill_proficiencies = set()
        self.weapon_proficiencies = set()
        self.armor_proficiencies = set()
        self.tool_proficiencies = set()
        self.features = set()

class Dwarf(Race):
    race_name = 'Dwarf'
    age_range = range(50, 350)
    height_range = range(48, 60)
    weight_range = range(100, 200)
    speed = 25

    def __init__(self):
        super().__init__()
        self.languages.add('Dwarvish')
        self.weapon_proficiencies |= {'battleaxes', 'handaxes', 'light hammers', 'warhammers'}
        self.tool_proficiencies.add(random.choice(['smith tools', 'brewer supplies', 'mason tools']))
        self.features |= {'Darkvision', 'Dwarven Resillience', 'Stonecunning'}
    
    @staticmethod
    def stat_bonuses():
        return {
            'Con': 2,
        }

class HillDwarf(Dwarf):
    race_name = 'Hill Dwarf'

    def __init__(self):
        super().__init__()
        self.features.add('Dwarven Toughness')
    
    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Wis'] = 1
        return bonuses

class MountainDwarf(Dwarf):
    race_name = 'Mountain Dwarf'

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor'}
    
    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Str'] = 1
        return bonuses

class Elf(Race):
    race_name = 'Elf'
    age_range = range(100, 750)
    height_range = range(60, 78)
    weight_range = range(100, 150)
    speed = 30

    def __init__(self):
        super().__init__()
        self.features |= {'Darkvision', 'Fey Ancestry', 'Trance'}
        self.languages.add('Elvish')
        self.skill_proficiencies.add('Perception')
    
    @staticmethod
    def stat_bonuses():
        return {
            'Dex': 2,
        }

class HighElf(Elf):
    race_name = 'High Elf'

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'longswords', 'shortswords', 'shortbows', 'longbows'}
        self.features.add('Cantrip')
        self.languages.add(random.choice(tables.languages))

    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Int'] = 1
        return bonuses

class WoodElf(Elf):
    race_name = 'Wood Elf'
    speed = 35

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'longswords', 'shortswords', 'shortbows', 'longbows'}
        self.features.add('Mask of the Wild')
    
    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Wis'] = 1
        return bonuses

class Drow(Elf):
    race_name = 'Drow'

    def __init__(self):
        super().__init__()
        self.features |= {'Superior Darkvision', 'Sunlight Sensitivity', 'Drow Magic'}
        self.weapon_proficiencies |= {'rapiers', 'shortswords', 'hand crossbows'}

    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Cha'] = 1
        return bonuses

class Halfling(Race):
    race_name = 'Halfling'
    age_range = range(20, 150)
    height_range = range(36, 40)
    weight_range = range(20, 50)
    speed = 25

    def __init__(self):
        super().__init__()
        self.features |= {'Lucky', 'Brave', 'Halfling Nimbleness'}
        self.languages.add('Halfling')

    @staticmethod
    def stat_bonuses():
        return {
            'Dex': 2,
        }

class LightfootHalfling(Halfling):
    race_name = 'Lightfoot Halfling'

    def __init__(self):
        super().__init__()
        self.features.add('Naturally Stealthy')

    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Cha'] = 1
        return bonuses

class StoutHalfling(Halfling):
    race_name = 'Stout Halfling'

    def __init__(self):
        super().__init__()
        self.features.add('Stout Resillience')

    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Con'] = 1
        return bonuses

class Human(Race):
    race_name = 'Human'
    age_range = range(18, 80)
    height_range = range(60, 78)
    weight_range = range(120, 200)
    speed = 30

    def __init__(self):
        super().__init__()
        self.languages.add(random.choice(tables.languages))

    @staticmethod
    def stat_bonuses():
        for stat in ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']:
            bonuses[stat] += 1
        return bonuses

class Dragonborn(Race):
    race_name = 'Dragonborn'
    age_range = range(15, 80)
    height_range = range(72, 90)
    weight_range = range(200, 300)
    speed = 30

    def __init__(self):
        super().__init__()
        self.languages.add('Draconic')
        self.features |= {'Breath Weapon', 'Damage Resistance'}
        self.ancestry = random.choice([
            'Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'
        ])

    @staticmethod
    def stat_bonuses():
        return {
            'Str': 1,
            'Dex': 1,
            'Con': 1,
            'Wis': 1,
            'Int': 1,
            'Cha': 1,
        }

    def __str__(self):
        return super().__str__() + f', ancestry: {self.ancestry}'

class Gnome(Race):
    race_name = 'Gnome'
    age_range = range(40, 500)
    height_range = range(36, 48)
    weight_range = range(20, 50)
    speed = 25

    def __init__(self):
        super().__init__()
        self.languages.add('Gnomish')
        self.features |= {'Darkvision', 'Gnome Cunning'}

    @staticmethod
    def stat_bonuses():
        return {
            'Int': 2,
        }

class ForestGnome(Gnome):
    race_name = 'Forest Gnome'

    def __init__(self):
        super().__init__()
        self.features |= {'Natural Illusionist', 'Speak With Small Beasts'}

    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Dex'] = 1
        return bonuses

class RockGnome(Gnome):
    race_name = 'Rock Gnome'

    def __init__(self):
        super().__init__()
        self.features |= {'Artificers Lore', 'Tinker'}
        self.tool_proficiencies.add('tinkers tools')

    @staticmethod
    def stat_bonuses():
        bonuses = super().stat_bonuses()
        bonuses['Con'] = 1
        return bonuses

class HalfElf(Race):
    race_name = 'Half Elf'
    age_range = range(20, 200)
    height_range = range(60, 78)
    weight_range = range(115, 180)
    speed = 30

    def __init__(self):
        super().__init__()
        self.languages.add('Elvish')
        self.features |= {'Darkvision', 'Fey Ancestry'}
        self.skill_proficiencies |= set(random.sample(tables.proficiency, 2))

    @staticmethod
    def stat_bonuses():
        random_bonuses = random.sample(['Str', 'Dex', 'Con', 'Wis', 'Int'], 2)
        total_bonuses = {bonus: 1 for bonus in random_bonuses}
        total_bonuses['Cha'] = 2
        return total_bonuses

class HalfOrc(Race):
    race_name = 'Half Orc'
    age_range = range(14, 75)
    height_range = range(72, 90)
    weight_range = range(150, 300)
    speed = 30

    def __init__(self):
        super().__init__()
        self.languages.add('Orc')
        self.features |= {'Darkvision', 'Menacing', 'Relentless Endurance', 'Savage Attacks'}
        self.skill_proficiencies.add('Intimidation')

    @staticmethod
    def stat_bonuses():
        return {
            'Str': 2,
            'Con': 1
        }

class Tiefling(Race):
    race_name = 'Tiefling'
    age_range = range(18, 85)
    height_range = range(60, 78)
    weight_range = range(120, 200)
    speed = 30

    def __init__(self):
        super().__init__()
        self.languages.add('Infernal')
        self.features |= {'Darkvision', 'Hellish Resistance', 'Infernal Legacy'}

    @staticmethod
    def stat_bonuses():
        return {
            'Cha': 2,
            'Int': 1
        }

all = [
    [HillDwarf, MountainDwarf], 
    [HighElf, WoodElf, Drow], 
    [LightfootHalfling, StoutHalfling], 
    [Human], 
    [Dragonborn], 
    [ForestGnome, RockGnome], 
    [HalfElf], 
    [HalfOrc], 
    [Tiefling]
]
