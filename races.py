import random
import tables

class Race:
    pass

class Dwarf(Race):
    race_name = 'Dwarf'
    age_range = range(50, 350)
    height_range = range(48, 60)
    weight_range = range(100, 200)
    speed = 25

    def __init__(self, class_):
        super().__init__(class_)
        self.languages.add('Dwarvish')
        self.weapon_proficiencies |= {'battleaxes', 'handaxes', 'light hammers', 'warhammers'}
        self.tool_proficiencies.add(random.choice(['smith tools', 'brewer supplies', 'mason tools']))
        self.racial_features |= {'Darkvision', 'Dwarven Resillience', 'Stonecunning'}
        self.stats['Con'] += 2

class HillDwarf(Dwarf):
    race_name = 'Hill Dwarf'

    def __init__(self, class_):
        super().__init__(class_)
        self.racial_features.add('Dwarven Toughness')
        self.stats['Wis'] += 1

class MountainDwarf(Dwarf):
    race_name = 'Mountain Dwarf'

    def __init__(self, class_):
        super().__init__(class_)
        self.armor_proficiencies |= {'light armor', 'medium armor'}
        self.stats['Str'] += 2

class Elf(Race):
    race_name = 'Elf'
    age_range = range(100, 750)
    height_range = range(60, 78)
    weight_range = range(100, 150)
    speed = 30

    def __init__(self, class_):
        super().__init__(class_)
        self.racial_features |= {'Darkvision', 'Fey Ancestry', 'Trance'}
        self.languages.add('Elvish')
        self.skill_proficiencies.add('Perception')
        self.stats['Dex'] += 2

class HighElf(Elf):
    race_name = 'High Elf'

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Int'] += 1
        self.weapon_proficiencies |= {'longswords', 'shortswords', 'shortbows', 'longbows'}
        self.racial_features.add('Cantrip')
        self.languages.add(random.choice(tables.languages))

class WoodElf(Elf):
    race_name = 'Wood Elf'
    speed = 35

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Wis'] += 1
        self.weapon_proficiencies |= {'longswords', 'shortswords', 'shortbows', 'longbows'}
        self.racial_features.add('Mask of the Wild')

class Drow(Elf):
    race_name = 'Drow'

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Cha'] += 1
        self.racial_features |= {'Superior Darkvisiclass_on', 'Sunlight Sensitivity', 'Drow Magic'}
        self.weapon_proficiencies |= {'rapiers', 'shortswords', 'hand crossbows'}

class Halfling(Race):
    race_name = 'Halfling'
    age_range = range(20, 150)
    height_range = range(36, 40)
    weight_range = range(20, 50)
    speed = 25

    def __init__(self, class_):
        super().__init__(class_)
        self.racial_features |= {'Lucky', 'Brave', 'Halfling Nimbleness'}
        self.languages.add('Halfling')
        self.stats['Dex'] += 2

class LightfootHalfling(Halfling):
    race_name = 'Lightfoot Halfling'

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Cha'] += 1
        self.racial_features.add('Naturally Stealthy')

class StoutHalfling(Halfling):
    race_name = 'Stout Halfling'

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Con'] += 1
        self.racial_features.add('Stout Resillience')

class Human(Race):
    race_name = 'Human'
    age_range = range(18, 80)
    height_range = range(60, 78)
    weight_range = range(120, 200)
    speed = 30

    def __init__(self, class_):
        super().__init__(class_)
        for stat in ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']:
            self.stats[stat] += 1
        self.languages.add(random.choice(tables.languages))

class Dragonborn(Race):
    race_name = 'Dragonborn'
    age_range = range(15, 80)
    height_range = range(72, 90)
    weight_range = range(200, 300)
    speed = 30

    def __init__(self, class_):
        super().__init__(class_)
        self.languages.add('Draconic')
        self.stats['Str'] += 2
        self.stats['Cha'] += 1
        self.racial_features |= {'Breath Weapon', 'Damage Resistance'}
        self.ancestry = random.choice([
            'Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White'
        ])

class Gnome(Race):
    race_name = 'Gnome'
    age_range = range(40, 500)
    height_range = range(36, 48)
    weight_range = range(20, 50)
    speed = 25

    def __init__(self, class_):
        super().__init__(class_)
        self.languages.add('Gnomish')
        self.stats['Int'] += 2
        self.racial_features |= {'Darkvision', 'Gnome Cunning'}

class ForestGnome(Gnome):
    race_name = 'Forest Gnome'

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Dex'] += 1
        self.racial_features |= {'Natural Illusionist', 'Speak With Small Beasts'}

class RockGnome(Gnome):
    race_name = 'Rock Gnome'

    def __init__(self, class_):
        super().__init__(class_)
        self.stats['Con'] += 1
        self.racial_features |= {'Artificers Lore', 'Tinker'}
        self.tool_proficiencies.add('tinkers tools')

class HalfElf(Race):
    race_name = 'Half Elf'
    age_range = range(20, 200)
    height_range = range(60, 78)
    weight_range = range(115, 180)
    speed = 30

    def __init__(self, class_):
        super().__init__(class_)
        self.languages.add('Elvish')
        self.stats['Cha'] += 2
        # Increase two random stats by 1
        for stat in random.sample(['Str', 'Dex', 'Con', 'Int', 'Wis',], 2):
            self.stats[stat] += 1

        self.racial_features |= {'Darkvision', 'Fey Ancestry'}
        self.skill_proficiencies |= set(random.sample(tables.proficiency, 2))

class HalfOrc(Race):
    race_name = 'Half Orc'
    age_range = range(14, 75)
    height_range = range(72, 90)
    weight_range = range(150, 300)
    speed = 30

    def __init__(self, class_):
        super().__init__(class_)
        self.languages.add('Orc')
        self.stats['Str'] += 2
        self.stats['Con'] += 1
        self.racial_features |= {'Darkvision', 'Menacing', 'Relentless Endurance', 'Savage Attacks'}
        self.skill_proficiencies.add('Intimidation')

class Tiefling(Race):
    race_name = 'Tiefling'
    age_range = range(18, 85)
    height_range = range(60, 78)
    weight_range = range(120, 200)
    speed = 30

    def __init__(self, class_):
        super().__init__(class_)
        self.languages.add('Infernal')
        self.stats['Cha'] += 2
        self.stats['Int'] += 1
        self.racial_features |= {'Darkvision', 'Hellish Resistance', 'Infernal Legacy'}

races = [
    HillDwarf,
    MountainDwarf,
    HighElf,
    WoodElf,
    Drow,
    LightfootHalfling,
    StoutHalfling,
    Human,
    Dragonborn,
    ForestGnome,
    RockGnome,
    HalfElf,
    HalfOrc,
    Tiefling,
]
