import random
from random import randint

# randomly choose a race and alter stat block accordingly
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
            'name':  'Dragonborn'
            'bonuses': {
                'Dex': 2,
                'Con': 1,
            },
            'age': range(20, 150),
            'height': range(36, 40),
            'weight': range(20, 50),
        },
    ]

    race = random.choice(races)
    race_name = race['name']
    age = random.choice(race['age'])
    height = random.choice(race['height'])

    for stat in race['bonuses']:
        stat_dict[stats] += race['bonuses'][stats]

    return race