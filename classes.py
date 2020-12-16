import random
import tables

class Class:
    proficiency_bonus = 2
    experience = 0

    def __init__(self):
        self.armor_proficiencies = set()
        self.weapon_proficiencies = set()
        self.skill_proficiencies = set()
        self.tool_proficiencies = set()
        self.save_throws = set()
        self.class_features = set()
        self.cantrips = set()
        self.spells = set()
        self.languages = set()

class Barbarian(Class):
    class_name = 'Barbarian'
    hit_dice = 12

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'heavy armor'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= {'Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'}
        self.save_throws |= {'Str', 'Con'}
        self.class_features |= {'Rage', 'Unarmored Defense'}

class Bard(Class):
    class_name = 'Bard'
    hit_dice = 8
    spell_slots = 2

    def __init__(self):
        super().__init__()
        self.armor_proficiencies.add('light armor')
        self.weapon_proficiencies |= {'simple weapons', 'hand crossbows', 'longswords', 'rapiers', 'shortswords'}
        self.tool_proficiencies.add('three musical instruments of your choice')
        self.skill_proficiencies |= set(random.sample(tables.proficiency, 3))
        self.save_throws |= {'Dex', 'Cha'}
        self.class_features.add('Bardic Inspiration')
        self.cantrips |= set(random.sample(tables.bard_cantrips, 2))
        self.spells |= set(random.sample(tables.bard_lvl1_spells, 4))

class Cleric(Class):
    class_name = 'Cleric'
    hit_dice = 8
    spell_slots = 2

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'shields'}
        self.weapon_proficiencies.add('simple weapons')
        self.skill_proficiencies |= set(random.sample(tables.proficiency, 2))
        self.save_throws |= {'Wis', 'Cha'}
        self.class_features.add('Channel Divinity')
        self.cantrips |= set(random.sample(tables.cleric_cantrips, 3))
        self.spells |= set(random.sample(tables.cleric_lvl1_spells, 2))
        self.domain = random.choice(['Knowledge Cleric', 'Divine Cleric', 'Light Cleric', 'Nature Cleric', 'Tempest Cleric', 'Trickery Cleric', 'War Cleric'])

        if self.domain == 'Knowledge Cleric':
            self.class_features.add('Bleesings of Knowledge')
            self.languages |= set(random.sample(tables.languages, 2))
            self.skill_proficiencies |= set(random.sample(['Arcana', 'History', 'Nature', 'Religion'], 2))
            self.spells |= {'Command', 'Identify'}
        
        elif self.domain == 'Divine Cleric':
            self.class_features.add('Disciple of Life')
            self.armor_proficiencies.add('heavy armor')
            self.spells |= {'Bless', 'Cure Wounds'}

        elif self.domain == 'Light Cleric':
            self.class_features.add('Warding Flare')
            self.spells |= {'Burning Hands', 'Faerie Fire'}
            self.cantrips |= set(random.choice(tables.cleric_cantrips))

        elif self.domain == 'Nature Cleric':
            self.armor_proficiencies.add('heavy armor')
            self.skill_proficiencies |= set(random.choice(['Animal Handling', 'Nature', 'Survival']))
            self.cantrips |= set(random.choice(tables.druid_cantrips))
            self.spells |= {'Animal Friendship', 'Speak with Animals'}

        elif self.domain == 'Tempest Cleric':
            self.armor_proficiencies.add('heavy armor')
            self.weapon_proficiencies.add('martial weapons')
            self.class_features.add('Wrath of the Storm')
            self.spells |= {'Fog Cloud', 'Thunderwave'}

        elif self.domain == 'Trickery Cleric':
            self.class_features.add('Blessing of the Trickster')
            self.spells |= {'Charm Person', 'Disguise Self'}

        elif self.domain == 'War Cleric':
            self.class_features.add('War Priest')
            self.armor_proficiencies.add('heavy armor')
            self.weapon_proficiencies.add('martial weapons')
            self.spells |= {'Divine Favor', 'Shield of Faith'}

class Druid(Class):
    class_name = 'Druid'
    hit_dice = 8
    spell_slots = 2

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'shields'}
        self.weapon_proficiencies |= {'clubs', 'daggers', 'javelins', 'maces', 'quarterstaffs', 'sickles', 'slings', 'spears'}
        self.tool_proficiencies.add('herbalism kit')
        self.skill_proficiencies |= set(random.sample(['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'], 2))
        self.save_throws |= {'Int', 'Wis'}
        self.cantrips |= set(random.sample(tables.druid_cantrips, 2))
        self.spells |= set(random.sample(tables.druid_lvl1_spells, 2))
        self.languages.add('Druidic')

class Fighter(Class):
    class_name = 'Fighter'
    hit_dice = 10

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'heavy armor', 'sheilds'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= set(random.sample(['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Preception', 'Survival'], 2))
        self.save_throws |= {'Str', 'Con'}
        self.class_features.add('Second Wind')
        self.fighting_style = random.choice(tables.fighter_styles)

class Monk(Class):
    class_name = 'Monk'
    hit_dice = 8

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'simple weapons', 'shortswords'}
        self.skill_proficiencies |= set(random.sample(['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'], 2))
        self.class_features |= {'Unarmored Defense', 'Martial Arts'}

class Paladin(Class):
    class_name = 'Paladin'
    hit_dice = 10

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'heavy armor'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= set(random.sample(['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'], 2))
        self.save_throws |= {'Wis', 'Cha'}
        self.class_features |= {'Divine Sense', 'Lay on Hands'}

class Ranger(Class):
    class_name = 'Ranger'
    hit_dice = 10
    favored_enemy = random.choice(tables.ranger_favored_enemy)
    favored_terrain = random.choice(tables.ranger_favored_terrain)

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'shields'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= set(random.sample(['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'], 3))
        self.class_features |= {'Favored Enemy', 'Natural Explorer'}

class Rogue(Class):
    class_name = 'Rogue'
    hit_dice = 8

    def __init__(self):
        super().__init__()
        self.armor_proficiencies.add('light armor')
        self.weapon_proficiencies |= {'simple weapons', 'hand crossbows', 'lonswords', 'rapiers', 'shortswords'}
        self.tool_proficiencies.add('thieves tools')
        self.skill_proficiencies |= set(random.sample(['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 
        'Performance', 'Persuasion', 'Slight of Hand', 'Stealth'], 4))
        self.class_features |= {'Expertise', 'Sneak Attack', 'Thieves Cant'}

class Sorcerer(Class):
    class_name = 'Sorcerer'
    hit_dice = 6
    spell_slots = 2

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'daggers', 'darts', 'slings', 'quarterstaffs', 'light crossbow'}
        self.skill_proficiencies |= set(random.sample(['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'], 2))
        self.cantrips |= set(random.sample(tables.sorcerer_cantrips, 4))
        self.spells |= set(random.sample(tables.sorcerer_lvl1_spells, 2))
        self.sorcerous_origin = random.choice(['Draconic Bloodline', 'Wild Magic'])
        if self.sorcerous_origin == 'Draconic Bloodine':
            self.class_features |= {'Draconic Ancestor', 'Draconic Resillience'}
        elif self. sorcerous_origin == 'Wild Magic':
            self.class_features |= {'Wild Magic Surge', 'Tides of Chaos'}

class Warlock(Class):
    class_name = 'Warlock'
    hit_dice = 8
    spell_slots = 1

    def __init__(self):
        super().__init__()
        self.armor_proficiencies.add('light armor')
        self.weapon_proficiencies.add('simple weapons')
        self.skill_proficiencies |= set(random.sample(['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion'], 2))
        self.save_throws |= {'Wis', 'Cha'}
        self.cantrips |= set(random.sample(tables.warlock_cantrips, 2))
        self.spells |= set(random.sample(tables.warlock_lvl1_spells, 2))
        self.patron = random.choice(['The Archfey', 'The Fiend', 'The Great Old One'])
        if self.patron == 'The Archfey':
            self.class_features.add('Fey Presence')
        elif self.patron == 'The Fiend':
            self.class_features.add('Dark ones Blessing')
        elif self.patron == 'The Great Old One':
            self.class_features.add('Awakened Mind')

class Wizard(Class):
    class_name = 'Wizard'
    hit_dice = 6
    spell_slots = 2

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'daggers', 'darts', 'slings', 'quarterstaff', 'light crossbows'}
        self.skill_proficiencies |= set(random.sample(['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'], 2))
        self.save_throws |= {'Int', 'Wis'}
        self.class_features.add('Arcane Recovery')
        self.arcane_tradition = random.choice(['School of Abjuration', 'School of Conjuration', 'School of Divination', 'School of Enchantment' 'School of Evocation', 'School of Illusion', 'School of Necromancy', 'School of Transmutation'])

        school = self.arcane_tradition.split()[-1]
        self.class_features.add(f'{school} Savant')

class_list = [
    Barbarian,
    Bard,
    Cleric,
    Druid,
    Fighter,
    Monk,
    Paladin,
    Ranger,
    Rogue,
    Sorcerer,
    Warlock,
    Wizard,
]
