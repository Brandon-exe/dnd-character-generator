import random

# randomly choose a class
def get_class():
    classes = [
        {
            'name': 'Barbarian',
            'hit dice': 12,
            'proficiencies': {
                'armor': {
                    'light armor', 'medium armor', 'shields',
                },
                'weapons': {
                    'simple weapons', 'martial weapons',
                },
                'tools': set(),
            },
            'saving throws': {
                'Str', 'Con',
            },
            'class features': {
                'Rage', 'Unarmored Defense',
            },
            'spells and cantrips': set(),
        },
        {
            'name': 'Bard',
            'hit dice': 8,
            'proficiencies': {
                'armor': {
                    'light armor',
                },
                'weapons': {
                    'simple weapons', 'hand crossbows', 'longswords', 'rapiers', 'shortswords',
                },
                'tools': {
                    'three musical instrucments of your choice'
                },
            },
            'saving throws': {
                'Dex', 'Cha',
            },
            'class features': {
                'Bardic Inspiration'
            },
            'spells and cantrips': {
                'cantrips known': 2,
                'spells known': 4,
            }
        },
        {
            'name': 'Cleric',
            'hit dice': 8,
            'proficiencies': {
                'armor': {
                    'light armor', 'medium armor', 'shields',
                },
                'weapons': {
                    'simple weapons',
                },
                'tools': set(),
            },
            'saving throws': {
                'Wis', 'Cha',
            },
            'class features': {
                'Bardic Inspiration'
            },
            'spells and cantrips': {
                'cantrips known': 2,
                'spells known': 4,
            }
        },
    ]
    char_class = random.choice(classes)
    return char_class