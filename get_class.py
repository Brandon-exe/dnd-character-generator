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
                    'bonus proficiency': 'heavy armor',
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
                        'Wrath of the Storm',
                    },
                    # add to proficiency list
                    'bonus proficiency': {
                        'heavy armor', 'martial weapons',
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
        {
            'name': 'Druid',
            'hit dice': 8,
            'proficiencies': {
                'armor': {
                'light armor', 'medium armor', 'shields',
                },
                'weapons': {
                    'clubs', 'daggers', 'javelins', 'maces', 'quarterstaffs', 'scimitars', 'sickles', 'slings', 'spears',
                },
                'tools': 'Herbalism Kit'
                # need to randomly choose two
                'skills': {
                    'Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival',
                },
                'saving throws': {
                'Int', 'Wis',
                },
            },
            'traits': set(),
            'languages': 'Druidic',
        },
        {
            'name': 'Fighter',
            'hit dice': 10,
            'proficiencies': {
                'armor': {
                    'light armor', 'medium armor', 'heavy armor', 'shields',
                },
                'weapons': {
                    'simple weapons', 'martial weapons',
                },
                'tools': set(),
                'saving throws': {
                    'Str', 'Con',
                },
                # need to randomly choose two
                'skills': {
                    'Acrobatics', 'Animal Handling', 'Athletics', 
                    'History', 'Insight', 'Intimidation', 'Perception', 'Survival',
                },
            },
            'traits': {
                'Second Wind',
            },
            # need to randomly choose one
            'Fighting Style': {
                'Archery', 'Defense', 'Dueling', 
                'Great Weapon Fighting', 'Protection',' Two-Weapon Fighting',
            },
        },
        {
            'name': 'Monk',
            'hit dice': 8,
            'proficiencies': {
                'armor': set(),
                'weapons': {
                    'simple weapons', 'shortswords',
                },
                'saving throws': {
                    'Str', 'Dex',
                },
                # need to randomly choose two
                'skills': {
                    'Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth',
                },
            },
            'traits': {
                'Unarmored Defense', 'Martial Arts',
            },
        },
        {
            'name': 'Paladin',
            'hit dice': 10,
            'proficiencies': {
                'armor': {
                    'light armor', 'medium armor', 'heavy armor',
                },
                'weapons': {
                    'simple weapons', 'martial weapons',
                },
                'tools': set(),
                'saving throws': {
                    'Wis', 'Cha',
                },
                # need to choose two randomly
                'skills': {
                    'Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion',
                },
            },
            'traits': {
                'Divine Sense', 'Lay on Hands',
            },
        },
        {
            'name': 'Ranger',
            'hit dice': 10,
            'proficiencies': {
                'armor': {
                    'light armor', 'medium armor', 'shields',
                },
                'weapons': {
                    'simple weapons', 'martial weapons',
                },
                'tools': set(),
                'saving throws': {
                    'Str', 'Dex',
                },
                # need to choose three randomly
                'skills': {
                    'Animal Handling', 'Athletics', 'Insight', 'Investigation', 
                    'Nature', 'Perception', 'Stealth', 'Survival',
                },
            },
            'traits': {
                # need to choose one randomly
                'Favored Enemy': {
                    'aberrations', 'beasts', 'celestials', 'constructs', 'dragons', 'elementals', 
                    'fey', 'fiends', 'giants', 'monstrosities', 'oozes', 'plants', 'undead',
                },
                # need to choose one randomly
                'Natural Explorer': {
                    'arctic', 'coast', 'desert', 'forest', 'grassland', 'mountain', 'swamp', 'Underdark',
                },
            },
        },
        {
            'name': 'Rogue',
            'hit dice': 8,
            'proficiencies': {
                'armor': 'light armor',
                'weapons': {
                    'simple weapons', 'hand crossbows', 'longswords', 'rapiers', 'shortswords',
                },
                'tools': 'thieves tools',
                'saving throws': {
                    'Dex', 'Int',
                },
                # need to choose four randomly
                'skills': {
                    'Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 
                    'Perception', 'Performance', 'Persuasion', 'Slight of Hand', 'Stealth',
                },
            },
            'traits': {
                'Expertise', 'Sneak Attack', 'Thieves Cant',
            },
        },
    ]
    char_class = random.choice(classes)
    return char_class