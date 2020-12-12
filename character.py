import random
from random import randint
from random import sample
from tables import alignment
from tables import languages
from tables import proficiency

# rolling the 4d6 for your stat
def roll_stat():
    stat_rolls = 4
    stat = [random.randint(1, 6) for i in range(stat_rolls)]
    stat.sort()
    del stat[0]
    return sum(stat)

# loops the roll_stat function to roll 4d6, remove the lowest roll, and repeats 6 times
def stats():
    stat_ttl = 6
    all_stats = [roll_stat() for i in range(stat_ttl)]
    return all_stats

class Character:
    def __init__(self):
        self.sex = random.choice(['Male', 'Female'])
        self.age = random.choice(self.age_range)
        self.height = random.choice(self.height_range)
        self.alignment = random.choice(alignment)
        self.languages = {'Common'}
        self.features = set()
        self.armor_proficiencies = set()
        self.weapon_proficiencies = set()
        self.tool_proficiencies = set()
        self.skill_proficiencies = set()
        self.save_throws = set()
        self.cantrips = set()
        self.spells = set()
        self.equipment = set()
        self.stats = dict(zip(['Str', 'Con', 'Dex', 'Int', 'Wis', 'Cha'], stats()))

class Dwarf(Character):
    race_name = 'Dwarf'
    age_range = range(50, 350)
    height_range = range(48, 60)
    weight_range = range(100, 200)
    speed = 25

    def __init__(self):
        super().__init__()
        self.languages.add('Dwarvish')
        self.weapon_proficiencies |= {'battleaxe', 'handaxe', 'light hammer', 'warhammer'}
        self.tool_proficiencies.add(random.choice(['smith tools', 'brewer supplies', 'mason tools']))
        self.features |= {'Darkvision', 'Dwarven Resillience', 'Stonecunning'}
        self.stats['Con'] += 2

class HillDwarf(Dwarf):
    race_name = 'Hill Dwarf'

    def __init__(self):
        super().__init__()
        self.features.add('Dwarven Toughness')
        self.stats['Wis'] += 1

class MountainDwarf(Dwarf):
    race_name = 'Mountain Dwarf'

    def __init__(self):
        super().__init__()
        self.armor_proficienies |= {'light armor', 'medium armor'}
        self.stats['Str'] += 2

class Elf(Character):
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
        self.stats['Dex'] += 2

class HighElf(Elf):
    race_name = 'High Elf'

    def __init__(self):
        super().__init__()
        self.stats['Int'] += 1
        self.weapon_proficiencies |= {'longsword', 'shortsword', 'shortbow', 'longbow'}
        self.features.add('Cantrip')
        self.languages.add(random.choice(languages))

class WoodElf(Elf):
    race_name = 'Wood Elf'
    speed = 35

    def __init__(self):
        super.__init__()
        self.stats['Wis'] += 1
        self.weapon_proficiencies |= {'longsword', 'shortsword', 'shortbow', 'longbow'}
        self.features.add('Mask of the Wild')

class Drow(Elf):
    race_name = 'Drow'

    def __init__(self):
        super.__init__()
        self.stats['Cha'] += 1
        self.features |= {'Superior Darkvision', 'Sunlight Sensitivity', 'Drow Magic'}
        self.weapon_proficiencies |= {'rapier', 'shortsword', 'hand crossbow'}

class Halfling(Character):
    race_name = 'Halfling'
    age_range = range(20, 150)
    height_range = range(36, 40)
    weight_range = range(20, 50)
    speed = 25

    def __init__(self):
        super.__init__()
        self.features |= {'Lucky', 'Brave', 'Halfling Nimbleness'}
        self.languages.add('Halfling')
        self.stats['Dex'] += 2

class LightfootHalfling(Halfling):
    race_name = 'Lightfoot Halfling'

    def __init__(self):
        super.__init__()
        self.stats['Cha'] += 1
        self.features.add('Naturally Stealthy')

class StoutHalfling(Halfling):
    race_name = 'Stout Halfling'

    def __init__(self):
        super.__init__()
        self.stats['Con'] += 1
        self.features.add('Stout Resillience')

class Human(Character):
    race_name = 'Human'
    age_range = range(18, 80)
    height_range = range(60, 78)
    weight_range = range(120, 200)
    speed = 30

    def __init__(self):
        super.__init__()
        self.stats['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha',] += 1
        self.languages.add(random.choice(languages))

class Dragonborn(Character):
    race_name = 'Dragonborn'
    age_range = range(15, 80)
    height_range = range(72, 90)
    weight_range = range(200, 300)
    speed = 30

    def __init__(self):
        super.__init__()
        self.languages.add('Draconic')
        self.stats['Str'] += 2
        self.stats['Cha'] += 1
        self.features |= {'Breath Weapon', 'Damage Resistance'}
        self.ancestry = random.choice([
            'Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'
        ])

class Gnome(Character):
    race_name = 'Gnome'
    age_range = range(40, 500)
    height_range = range(36, 48)
    weight_range = range(20, 50)
    speed = 25

    def __init__(self):
        super.__init__()
        self.languages.add('Gnomish')
        self.stats['Int'] += 2
        self.features |= {'Darkvision', 'Gnome Cunning'}

class ForestGnome(Gnome):
    race_name = 'Forest Gnome'

    def __init__(self):
        super.__init__()
        self.stats['Dex'] += 1
        self.features |= {'Natural Illusionist', 'Speak With Small Beasts'}

class RockGnome(Gnome):
    race_name = 'Rock Gnome'

    def __init__(self):
        super.__init__()
        self.stats['Con'] += 1
        self.features |= {'Artificers Lore', 'Tinker'}
        self.tool_proficiencies.add('tinkers tools')

class HalfElf(Character):
    race_name = 'Half Elf'
    age_range = range(20, 200)
    height_range = range(60, 78)
    weight_range = range(115, 180)
    speed = 30

    def __init__(self):
        super.__init__()
        self.languages.add('Elvish')
        self.stats['Cha'] += 2
        self.stats(random.sample(['Str', 'Dex', 'Con', 'Int', 'Wis',], 2)) += 1
        self.featrues |= {'Darkvision', 'Fey Ancestry'}
        self.skill_proficiencies.add(random.sample(proficiency, 2))

class HalfOrc(Character):
    race_name = 'Half Orc'
    age_range = range(14, 75)
    height_range = range(72, 90)
    weight_range = range(150, 300)
    speed = 30

    def __init__(self):
        super.__init__()
        self.languages.add('Orc')
        self.stats['Str'] += 2
        self.stats['Con'] += 1
        self.features |= {'Darkvision', 'Menacing', 'Relentless Endurance', 'Savage Attacks'}
        self.skill_proficiancies.add('Intimidation')

class Tiefling(Character):
    race_name = 'Tiefling'
    age_range = range(18, 85)
    height_range = range(60, 78)
    weight_range = range(120, 200)
    speed = 30

    def __init__(self):
        super.__init__()
        self.languages.add('Infernal')
        self.stats['Cha'] += 2
        self.stats['Int'] += 1
        self.features |= {'Darkvision', 'Hellish Resistance', 'Infernal Legacy'}