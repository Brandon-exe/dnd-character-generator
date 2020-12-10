import random
from random import sample
from random import randint

# randomly generate a race and its physical attributes and alter stat block accordingly
def get_race(stat_dict):

    races = [
        {
            'name': 'Hill Dwarf',
            'bonuses': {
                'Con': 2,
                'Wis': 1,
            },
            'traits': {
                'Darkvision', 'Dwarven Resilience', 'Stonecunning',
            },
            'proficiency': {
                'weapons': {
                    'battleaxe', 'handaxe', 'light hammer', 'warhammer',
                },
                # need to choose one randomly
                'tools': {
                    'smiths tools', 'brewer supplies', 'mason tools',
                },
            },
            'age': range(50, 350),
            'height': range(48, 60),
            'weight': range(100, 200),
            'speed': 25,
            'languages': {
                'Common', 'Dwarvish',
            },
        },
        {
            'name': 'Mountain Dwarf',
            'bonuses': {
                'Con': 2,
                'Wis': 1,
            },
            'traits': {
                'Darkvision', 'Dwarven Resilience', 'Stonecunning',
            },
            'proficiency': {
                'weapons': {
                    'battleaxe', 'handaxe', 'light hammer', 'warhammer',
                },
                # Need to choose one randomly
                'tools': {
                    'smiths tools', 'brewer supplies', 'mason tools',
                },
            },
            'age': range(50, 350),
            'height': range(48, 60),
            'weight': range(100, 200),
            'speed': 25,
            'languages': {
                'Common', 'Dwarvish',
            },
        },
        {
            'name': 'High Elf',
            'bonuses': {
                'Dex': 2,
                'Int': 1,
            },
            'traits': {
                'Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', 'Cantrip', 'Extra Language',
            },
            'proficiency': {
                'weapons': {
                    'longsward', 'shortsword', 'shortbow', 'longbow',
                },
            },
            'age': range(100, 750),
            'height': range(60, 78),
            'weight': range(100, 150),
            'speed': 30,
            'languages': {
                'Common', 'Elvish',
            },
        },
        {
            'name': 'Wood Elf',
            'bonuses': {
                'Dex': 2,
                'Wis': 1,
            },
            'traits': {
                'Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', 'Mask of the Wild',
            },
            'proficiency': {
                'weapons': {
                    'longsword', 'shortsword', 'shortbow', 'longbow',
                },
            },
            'age': range(100, 750),
            'height': range(60, 78),
            'weight': range(100, 150),
            'speed': 35,
            'languages': {
                'Common', 'Elvish',
            },
        },
        {
            'name': 'Drow',
            'bonuses': {
                'Dex': 2,
                'Cha': 1,
            },
            'traits': {
                'Superior Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', 'Drow Magic', 'Sunlight Sensitivity',
            },
            'proficiancy': {
                'weapons': {
                    'rapiers', 'shortswords', 'hand crossbows'
                },
            },
            'age': range(100, 750),
            'height': range(60, 78),
            'weight': range(100, 150),
            'speed': 30,
            'languages': {
                'Common', 'Elvish'
            },
        },
        {
            'name': 'Lightfood Halfling',
            'bonuses': {
                'Dex': 2,
                'Cha': 1,
            },
            'traits': {
                'Lucky', 'Brave', 'Halfling Nimbleness', 'Naturally Stealthy',
            },
            'age': range(20, 150),
            'height': range(36, 40),
            'weight': range(20, 50),
            'speed': 25,
            'laungages': {
                'Common', 'Halfling'
            },
        },
        {
            'name': 'Stout Halfling',
            'bonuses': {
                'Dex': 2,
                'Con': 1,
            },
            'traits': {
                'Lucky', 'Brave', 'Halfling Nimbleness', 'Stout Resilience',
            },
            'age': range(20, 150),
            'height': range(36, 40),
            'weight': range(20, 50),
            'speed': 25,
            'laungages': {
                'Common', 'Halfling'
            },
        },
        {
            'name': 'Human',
            'bonuses': {
                'Str': 1,
                'Con': 1,
                'Dex': 1,
                'Int': 1,
                'Wis': 1,
                'Cha': 1,
            },
            'age': range(18, 80),
            'height': range(60, 78),
            'weight': range(120, 200),
            'speed': 30,
            # need one randomized language
            'languages': {
                'Common',
            },
        },
        {
            'name':  'Dragonborn',
            'bonuses': {
                'Str': 2,
                'Cha': 1,
            },
            'traits': {
                'Breath Weapon', 'Damage Resistance',
            },
            'random traits': {
                'ancestry': {
                    'Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold',
                    'Green', 'Red', 'Silver', 'White'
                }
            },
            'age': range(15, 80),
            'height': range(72, 90),
            'weight': range(200, 300),
            'speed': 30,
            'languages': {
                'Common', 'Draconic'
            },
        },
        {
            'name':  'Forest Gnome',
            'bonuses': {
                'Int': 2,
                'Dex': 1,
            },
            'traits': {
                'Darkvision', 'Gnome Cunning', 'Natural Illusionist', 'Speak with Small Beasts',
            },
            'age': range(40, 500),
            'height': range(36, 48),
            'weight': range(20, 50),
            'speed': 25,
            'languages': {
                'Common', 'Gnomish',
            },
        },
        {
            'name':  'Rock Gnome',
            'bonuses': {
                'Int': 2,
                'Con': 1,
            },
            'random traits': {
                'Clockwork Toy', 'Fire Starter', 'Music Box',
            },
            'traits': {
                'Artificers Lore', 'Tinker',
            },
            'proficiancy': {
                'tinkers tools'
            },
            'age': range(40, 500),
            'height': range(36, 48),
            'weight': range(20, 50),
            'speed': 25,
            'languages': {
                'Common', 'Gnomish',
            },
        },
        {
            'name':  'Half-Elf',
            # need randomized +1 in 2 other ability scores
            'bonuses': {
                'Cha': 2,
            },
            'traits': {
                'Darkvision', 'Fey Ancestry',
            },
            # need two random skill proficiancies
            'random proficiancy': {
                'Athletics', 'Acrobatics', 'Sleight of Hand', 'Stealth',
                'Arcana', 'History', 'Investigation', 'Nature', 'Nature',
                'Religion', 'Animal Handling' 'Insight', 'Medicine',
                'Perception', 'Survival', 'Deception', 'Intimidation',
                'Performance', 'Persuasion',
            },
            'age': range(20, 200),
            'height': range(60, 78),
            'weight': range(115, 180),
            'speed': 30,
            # need one randomized language
            'languages': {
                'Common', 'Elvish',
            },
        },
        {
            'name':  'Half-Orc',
            'bonuses': {
                'Str': 2,
                'Con': 1,
            },
            'traits': {
                'Darkvision', 'Menacing', 'Relentless Endurance', 'Savage Attacks',
            },
            'proficiancy': {
                'skills': {'intimidation'},
            },
            'age': range(14, 75),
            'height': range(72, 90),
            'weight': range(150, 300),
            'speed': 30,
            'languages': {
                'Common', 'Orc',
            },
        },
        {
            'name':  'Tiefling',
            'bonuses': {
                'Cha': 2,
                'Int': 1,
            },
            # need to add spells from "infernal legacy" trait to spell list.
            'traits': {
                'Darkvision', 'Hellish Resistance', 'Infernal Legacy',
            },
            'age': range(18, 85),
            'height': range(60, 78),
            'weight': range(120, 200),
            'speed': 30,
            'languages': {
                'Common', 'Infernal',
            },
        },
    ]

    race = random.choice(races)
    race_name = races['name']
    age = random.choice(races['age'])
    height = random.choice(races['height'])
    weight = random.choice(races['weight'])

    for stat, bonus in races['bonuses'].items():
        stat_dict[stat] += bonus

    return race
