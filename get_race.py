import random
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
            'age': range(50, 350),
            'height': range(48, 60)
            'weight': range(100, 200),
        },
        {
            'name': 'Mountain Dwarf',
            'bonuses': {
                'Con': 2,
                'Str': 2,
            },
            'age': range(50, 350),
            'height': range(48, 60),
            'weight': range(100, 200),
        },
        {
            'name': 'High Elf',
            'bonuses': {
                'Dex': 2,
                'Int': 1,
            },
            'age': range(100, 750),
            'height': range(60, 78),
            'weight': range(100, 150),
        },
        {
            'name': 'Wood Elf',
            'bonuses': {
                'Dex': 2,
                'Wis': 1,
            },
            'age': range(100, 750),
            'height': range(60, 78),
            'weight': range(100, 150),
        },
        {
            'name': 'Drow',
            'bonuses': {
                'Dex': 2,
                'Cha': 1,
            },
            'age': range(100, 750),
            'height': range(60, 78),
            'weight': range(100, 150),
        },
        {
            'name': 'Lightfood Halfling',
            'bonuses': {
                'Dex': 2,
                'Cha': 1,
            },
            'age': range(20, 150),
            'height': range(36, 40),
            'weight': range(20, 50),
        },
        {
            'name': 'Stout Halfling',
            'bonuses': {
                'Dex': 2,
                'Con': 1,
            },
            'age': range(20, 150),
            'height': range(36, 40),
            'weight': range(20, 50),
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
        },
        {
            'name':  'Dragonborn',
            'bonuses': {
                'Str': 2,
                'Cha': 1,
            },
            'age': range(15, 80),
            'height': range(72, 90),
            'weight': range(200, 300),
        },
        {
            'name':  'Forest Gnome',
            'bonuses': {
                'Int': 2,
                'Dex': 1,
            },
            'age': range(40, 500),
            'height': range(36, 48),
            'weight': range(20, 50),
        },
        {
            'name':  'Rock Gnome',
            'bonuses': {
                'Int': 2,
                'Con': 1,
            },
            'age': range(40, 500),
            'height': range(36, 48),
            'weight': range(20, 50),
        },
        {
            'name':  'Half-Elf',
            'bonuses': {
                'Cha': 2,
            },
            'age': range(20, 200),
            'height': range(60, 78),
            'weight': range(115, 180),
        },
        {
            'name':  'Half-Orc',
            'bonuses': {
                'Str': 2,
                'Con': 1,
            },
            'age': range(14, 75),
            'height': range(72, 90),
            'weight': range(150, 300),
        },
        {
            'name':  'Tiefling',
            'bonuses': {
                'Cha': 2,
                'Int': 1,
            },
            'age': range(18, 85),
            'height': range(60, 78),
            'weight': range(120, 200),
        },
    ]

    race = random.choice(races)
    race_name = race['name']
    age = random.choice(race['age'])
    height = random.choice(race['height'])

    for stat in race['bonuses']:
        stat_dict[stats] += race['bonuses'][stats]

    return race