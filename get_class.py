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
                # use random.sample() here to choose two random skills
                'skills': {
                    'Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival',
                },
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
                # use random.sample() here to choose 3 random skills
                'skills': {
                    'Athletics', 'Acrobatics', 'Sleight of Hand', 'Stealth', 'Arcana', 
                    'History', 'Investigation', 'Nature', 'Nature', 'Religion', 'Animal Handling'
                    'Insight', 'Medicine', 'Perception', 'Survival', 'Deception', 'Intimidation',
                    'Performance', 'Persuasion',
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
                # use random.sample() here to choose two skills
                'skills': {
                    'History', 'Insight', 'Medicine', 'Persuasion', 'Religion',
                },
            },
            'saving throws': {
                'Wis', 'Cha',
            },
            # use random.sample() here to choose one divine domain
            'divine domain': {
                'Knowledge': {
                    'traits': 'Blessings of Knowledge',
                    'domain spells': {
                        'command', 'identify',
                    },
                }, 
                'Life': {
                    'traits': {
                        'Disciple of Life',
                    },
                        # add to proficiency list
                    'bonus proficiency': 'heavy armor',
                    'domain spells': {
                        'bless', 'cure wounds',
                    },
                }, 
                'Light': {
                    'traits': {
                        # add extra cantrip to spells known
                        'bonus cantrip',
                        'Warding Flare'
                    },
                    'domain spells': {
                        'burning hands',
                        'faerie fire',
                    },
                }, 
                'Nature': {
                    # add to proficiency list
                    'bonus proficiency': 'heavy armor'
                    # gain one druid cantrip, use random to gain one of the following skill proficiencies
                    'Acolyte of Nature': {
                        'Animal Handling', 'Nature', 'Survival',
                    },
                    'domain spells': {
                        'animal friendship', 'speak with animals',
                    },
                }, 
                'Tempest': {
                    'traits': {
                        # add to proficiency list
                        'bonus proficiency': {
                            'heavy armor', 'martial weapons',
                        },
                        'Wrath of the Storm',
                    },
                    'domain spells': {
                        'fog cloud', 'thunderwave',
                    },
                }, 
                'Trickery': {
                    'traits': 'Blessing of the Trickster',
                    'domain spells': {
                        'charm person', 'disguise self',
                    },
                }, 
                'War': {
                    'traits': {
                        'War Priest',
                    },
                    'bonus proficiency': {
                        # add to proficiency list
                        'heavy armor', 'martial weapons',
                    },
                    'domain spells': {
                        'divine favor', 'shield of faith',
                    },
                },
            },
            'spells and cantrips': {
                'cantrips known': 3,
                'spells known': 2,
            }
        },
    ]
    char_class = random.choice(classes)
    return char_class