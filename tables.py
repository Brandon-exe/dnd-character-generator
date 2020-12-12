proficiency = [
    'Athletics', 'Acrobatics', 'Sleight of Hand', 'Stealth',
    'Arcana', 'History', 'Investigation', 'Nature', 'Nature',
    'Religion', 'Animal Handling' 'Insight', 'Medicine',
    'Perception', 'Survival', 'Deception', 'Intimidation',
    'Performance', 'Persuasion',
]

alignment = [
    'Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Good', 'Neutral', 
    'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil',
]

languages = [
    'Common', 'Dwarvish', 'Elvish', 'Giant', 'Gnomish', 'Goblin', 'Halfling', 'Orc', 'Abyssal', 
    'Celestial', 'Deep Speech', 'Draconic', 'Infernal', 'Primordial', 'Sylvan', 'Undercommon',
]

attributes = [
    'Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha',
]

armor = [
    {
        'light armor': {
            'padded', 'leather', 'studded leather',
        },
        'medium armor': {
            'hide', 'chain shirt', 'scale mail', 'breastplate', 'half plate',
        },
        'heavy armor': {
            'ring mail', 'chain mail', 'splint', 'plate',
        },
        'shield': {
            'shield',
        }
    },
]

weapons = [
    {
        'simple weapons': {
            'club', 'dagger', 'greatclub', 'handaxe', 'javelin', 'light hammer', 'mace', 
            'quarterstaff', 'sickle', 'spear', 'light crossbow', 'dart', 'shortbow', 'sling',
        },
        'martial weapons': {
            'battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword', 'halberd', 'lance', 'longsword', 'maul', 'morningstar',
            'pike', 'rapier', 'scimitar', 'shortsword', 'trident', 'war pick', 'warhammer', 'whip', 'blowgun', 'hand crossbow',
            'heavy crossbow', 'longbow', 'net',
        },
    },
]

backgrounds = [
    {
        'name': 'Acolyte',
        'proficiencies': {
            'Insight', 'Religion',
        },
        'traits': {
            'personality': {
                '''I idolize a particular hero of my faith, and constantly refer to that person's deeds and example.''',
                '''I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.''',
                '''I see omens in every event and action. The gods try to speak to us, we just need to listen.''',
                '''Nothing can shake my optimistic attitude.''',
                '''I quote (or misquote) sacred texts and proverbs in almost every situation.''',
                '''I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.''',
                '''I've enjoyed fin food, drink, and high society among my temple's elite. Rough living grates on me.''',
                '''I've spent so long in the temple that I have little practical experience dealing with people in the outside world.''',
            },
            'ideal': {
                'Tradition', 'Charity', 'Change', 'Power', 'Faith', 'Aspiration',
            },
            'bond': {
                '''I would die to recover an ancient relic of my faith that was lost long ago.''',
                '''I will someday get revenge on the corrupt temple hierarchy who randed my a heretic''',
                '''I owe my life to the priest who took me in when my parents died.''',
                '''Everything I do is for the common people''',
                '''I will do anything to protect the temple where I served''',
                '''I seek to preserve a sacred text that my enemies consider heretical and seek to destroy''',
            },
            'flaw': {
                '''I judge others harshly, and myself even more severely.''',
                '''I put too much trust in those who wield power within my temple's hierarchy.''',
                '''My piety sometimes leads me to blindly trust those that profess faith in my god.''',
                '''I am inflexible in my thinking.''',
                '''I am suspicious of strangers and expect the worst of them.''',
                '''Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.''',
            },
        },
    },
    {
        'name': 'Charlatan',
        'proficiencies': {
            'skills': {
                'Deception', 'Slight of Hand',
            },
            'tools': {
                'disguise kit', 'forgery kit',
            },
        },
        'favorite scam': {
            '''cheat at games.''',
            '''shave coins and forge documents.''',
            '''insinuate into people's lives to secure their fortunes.''',
            '''forged identities''',
            '''sleight-of-hand cons''',
            '''convince people that worthless junk is worth money.''',
        },
    },
]

