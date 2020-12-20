import random
import tables
import character

class Class:
    proficiency_bonus = 2
    experience = 0
    spell_slots = 0

    def __init__(self):
        self.armor_proficiencies = set()
        self.weapon_proficiencies = set()
        self.skill_proficiencies = set()
        self.tool_proficiencies = set()
        self.saving_throws = set()
        self.class_features = set()
        self.cantrips = set()
        self.spells = set()
        self.languages = set()
    
    def __str__(self):
        return f'Class {self.class_name}, hit die 1d{self.hit_dice}'
    
    def spell_save_dc(self, character):
        return None

    def spell_attack_modifier(self, character):
        return None

class Barbarian(Class):
    class_name = 'Barbarian'
    hit_dice = 12
    stat_preference = ['Str', 'Con', 'Dex', 'Cha', 'Wis', 'Int']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'heavy armor'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= {'Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'}
        self.saving_throws |= {'Str', 'Con'}
        self.class_features |= {'Rage', 'Unarmored Defense'}

    def starting_equipment(self):
        all_equipment = {'explorers pack', 'x4 javelins',}
        all_equipment.add(random.choice(['battleaxe', random.choice(tables.martial_weapons)]))
        all_equipment.add(random.choice(['two handaxes', random.choice(tables.simple_weapons)]))
        return all_equipment


class Bard(Class):
    class_name = 'Bard'
    hit_dice = 8
    spell_slots = 2
    stat_preference = ['Cha', 'Dex', 'Wis', 'Int', 'Con', 'Str']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies.add('light armor')
        self.weapon_proficiencies |= {'simple weapons', 'hand crossbows', 'longswords', 'rapiers', 'shortswords'}
        self.tool_proficiencies.add('three musical instruments of your choice')
        self.skill_proficiencies |= set(random.sample(tables.proficiency, 3))
        self.saving_throws |= {'Dex', 'Cha'}
        self.class_features.add('Bardic Inspiration')
        self.cantrips |= set(random.sample(tables.bard_cantrips, 2))
        self.spells |= set(random.sample(tables.bard_lvl1_spells, 4))

    def starting_equipment(self):
        all_equipment = {'leather armor', 'dagger',}
        all_equipment.add(random.choice(['rapier', 'longsword', random.choice(tables.simple_weapons)]))
        all_equipment.add(random.choice(['diplomats pack', 'entertainers pack',]))
        all_equipment.add(random.choice(['lute', random.choice(tables.instruments)]))
        return all_equipment

    def spell_save_dc(self, character):
        return 8 + self.proficiency_bonus + character.stats['Cha'].modifier
    
    def spell_attack_modifier(self, character):
        return self.proficiency_bonus + character.stats['Cha'].modifier

class Cleric(Class):
    class_name = 'Cleric'
    hit_dice = 8
    spell_slots = 2
    stat_preference = ['Wis', 'Str', 'Con', 'Cha', 'Int', 'Dex']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'shields'}
        self.weapon_proficiencies.add('simple weapons')
        self.skill_proficiencies |= set(random.sample(tables.proficiency, 2))
        self.saving_throws |= {'Wis', 'Cha'}
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
            self.cantrips.add(random.choice(tables.cleric_cantrips))

        elif self.domain == 'Nature Cleric':
            self.armor_proficiencies.add('heavy armor')
            self.skill_proficiencies |= set(random.choice(['Animal Handling', 'Nature', 'Survival']))
            self.cantrips.add(random.choice(tables.druid_cantrips))
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
    
    def starting_equipment(self):
        all_equipment = {'shield', 'holy symbol'}
        all_equipment |= random.choice([{'light crossbow', 'x20 bolts'}, {random.choice(tables.simple_weapons)}])
        all_equipment.add(random.choice(['priests pack', 'explorers pack']))

        if 'warhammer' in self.weapon_proficiencies:
            all_equipment.add(random.choice(['mace', 'warhammer']))
        else:
            all_equipment.add('mace')
        if 'chain mail' in self.armor_proficiencies:
            all_equipment.add(random.choice(['scale mail', 'leather armor', 'chain mail']))
        else:
            all_equipment.add(random.choice(['scale mail', 'leather armor']))
        return all_equipment

    def spell_save_dc(self, character):
        return 8 + self.proficiency_bonus + character.stats['Wis'].modifier

    def spell_attack_modifier(self, character):
        return self.proficiency_bonus + character.stats['Wis'].modifier
        
    def __str__(self):
        return super().__str__() + f', domain: {self.domain}'

class Druid(Class):
    class_name = 'Druid'
    hit_dice = 8
    spell_slots = 2
    stat_preference = ['Wis', 'Con', 'Dex', 'Int', 'Cha', 'Str']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'shields'}
        self.weapon_proficiencies |= {'clubs', 'daggers', 'javelins', 'maces', 'quarterstaffs', 'sickles', 'slings', 'spears'}
        self.tool_proficiencies.add('herbalism kit')
        self.skill_proficiencies |= set(random.sample(['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'], 2))
        self.saving_throws |= {'Int', 'Wis'}
        self.cantrips |= set(random.sample(tables.druid_cantrips, 2))
        self.spells |= set(random.sample(tables.druid_lvl1_spells, 2))
        self.languages.add('Druidic')

    def starting_equipment(self):
        all_equipment = {'leather armor', 'explorers pack', 'druidic focus'}
        simple_melee_weapon = random.choice(['club', 'dagger', 'greatclub', 'handaxe', 'light hammer', 'mace', 'quarterstaff', 'sickle'])
        all_equipment.add(random.choice(['wooden shield', random.choice(tables.simple_weapons)]))
        all_equipment.add(random.choice(['scimitar', simple_melee_weapon]))
        return all_equipment

    def spell_save_dc(self, character):
        return 8 + self.proficiency_bonus + character.stats['Wis'].modifier

    def spell_attack_modifier(self, character):
        return self.proficiency_bonus + character.stats['Wis'].modifier

class Fighter(Class):
    class_name = 'Fighter'
    hit_dice = 10
    stat_preference = ['Str', 'Dex', 'Con', 'Cha', 'Wis', 'Int']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'heavy armor', 'sheilds'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= set(random.sample(['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Preception', 'Survival'], 2))
        self.saving_throws |= {'Str', 'Con'}
        self.class_features.add('Second Wind')
        self.fighting_style = random.choice(tables.fighter_styles)
    
    def starting_equipment(self):
        all_equipment = set()
        shield_and_martial_weapon = {'shield', random.choice(tables.martial_weapons)}
        two_martial_weapons = set(random.sample(tables.martial_weapons, 2))
        all_equipment |= random.choice([shield_and_martial_weapon, two_martial_weapons])
        all_equipment |= random.choice([{'chain mail'}, {'longbow', 'leather armor', 'x20 arrows'}])
        all_equipment |= random.choice([{'light crossbow', 'x20 bolts'}, {'x2 hand axe'}])
        all_equipment.add(random.choice(['dungeoneers pack', 'explorers pack']))
        return all_equipment

class Monk(Class):
    class_name = 'Monk'
    hit_dice = 8
    stat_preference = ['Dex', 'Wis', 'Str', 'Con', 'Int', 'Cha']

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'simple weapons', 'shortswords'}
        self.skill_proficiencies |= set(random.sample(['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'], 2))
        self.saving_throws |= {'Str', 'Dex'}
        self.class_features |= {'Unarmored Defense', 'Martial Arts'}

    def starting_equipment(self):
        all_equipment = {'10 darts'}
        all_equipment |= random.choice([{'shortsword', random.choice(tables.simple_weapons)}])
        all_equipment.add(random.choice(['dungeoneers pack', 'explorers pack']))
        return all_equipment

class Paladin(Class):
    class_name = 'Paladin'
    hit_dice = 10
    stat_preference = ['Str', 'Cha', 'Con', 'Wis', 'Int', 'Dex']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'heavy armor'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= set(random.sample(['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'], 2))
        self.saving_throws |= {'Wis', 'Cha'}
        self.class_features |= {'Divine Sense', 'Lay on Hands'}
    
    def starting_equipment(self):
        all_equipment = {'chain mail', 'holy symbol'}
        shield_and_martial_weapon = {'shield', random.choice(tables.martial_weapons)}
        two_martial_weapons = set(random.sample(tables.martial_weapons, 2))
        simple_melee_weapon = random.choice(['club', 'dagger', 'greatclub', 'handaxe', 'light hammer', 'mace', 'quarterstaff', 'sickle'])
        all_equipment.add(random.choice(['x5 javelins', simple_melee_weapon]))
        all_equipment.add(random.choice(['priests pack', 'explorers pack']))
        all_equipment |= (random.choice([shield_and_martial_weapon, two_martial_weapons]))
        return all_equipment

class Ranger(Class):
    class_name = 'Ranger'
    hit_dice = 10
    favored_enemy = random.choice(tables.ranger_favored_enemy)
    favored_terrain = random.choice(tables.ranger_favored_terrain)
    stat_preference = ['Dex', 'Wis', 'Str', 'Con', 'Int', 'Cha']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies |= {'light armor', 'medium armor', 'shields'}
        self.weapon_proficiencies |= {'simple weapons', 'martial weapons'}
        self.skill_proficiencies |= set(random.sample(['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'], 3))
        self.saving_throws |= {'Str', 'Dex'}
        self.class_features |= {'Favored Enemy', 'Natural Explorer'}
    
    def starting_equipment(self):
        all_equipment = {'longbow', 'x20 arrows', 'quiver'}
        simple_melee_weapon = random.choice(['club', 'dagger', 'greatclub', 'handaxe', 'light hammer', 'mace', 'quarterstaff', 'sickle'])
        all_equipment.add(random.choice(['x2 shortsword', simple_melee_weapon]))
        all_equipment.add(random.choice(['scale mail', 'leather armor']))
        all_equipment.add(random.choice(['dungeoneers pack', 'explorers pack']))
        return all_equipment
    
    def __str__(self):
        return super().__str__() + f', favored terrain: {self.favored_terrain}, favored enemy: {self.favored_enemy}'

class Rogue(Class):
    class_name = 'Rogue'
    hit_dice = 8
    stat_preference = ['Dex', 'Cha', 'Int', 'Con', 'Str', 'Wis']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies.add('light armor')
        self.weapon_proficiencies |= {'simple weapons', 'hand crossbows', 'longswords', 'rapiers', 'shortswords'}
        self.tool_proficiencies.add('thieves tools')
        self.skill_proficiencies |= set(random.sample(['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 
        'Performance', 'Persuasion', 'Slight of Hand', 'Stealth'], 4))
        self.saving_throws |= {'Dex', 'Int'}
        self.class_features |= {'Expertise', 'Sneak Attack', 'Thieves Cant'}

    def starting_equipment(self):
        all_equipment = {'leather amror', 'two daggers', 'thieves tools'}
        all_equipment |= random.choice([{'shortbow', 'x20 arrows', 'quiver'}, {'shortsword'}])
        all_equipment.add(random.choice(['rapier', 'shortsword']))
        all_equipment.add(random.choice(['burglars pack', 'dungeoneers pack', 'explorers pack']))
        return all_equipment

class Sorcerer(Class):
    class_name = 'Sorcerer'
    hit_dice = 6
    spell_slots = 2
    stat_preference = ['Cha', 'Con', 'Int', 'Wis', 'Dex', 'Str']

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'daggers', 'darts', 'slings', 'quarterstaffs', 'light crossbow'}
        self.skill_proficiencies |= set(random.sample(['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'], 2))
        self.saving_throws |= {'Cha', 'Con'}
        self.cantrips |= set(random.sample(tables.sorcerer_cantrips, 4))
        self.spells |= set(random.sample(tables.sorcerer_lvl1_spells, 2))
        self.sorcerous_origin = random.choice(['Draconic Bloodline', 'Wild Magic'])
        if self.sorcerous_origin == 'Draconic Bloodine':
            self.class_features |= {'Draconic Ancestor', 'Draconic Resillience'}
        elif self. sorcerous_origin == 'Wild Magic':
            self.class_features |= {'Wild Magic Surge', 'Tides of Chaos'}
    
    def starting_equipment(self):
        all_equipment = {'x2 daggers'}
        all_equipment.add(random.choice(['component pouch', 'arcane focus']))
        all_equipment.add(random.choice(['dungeoneers pack', 'explorers pack']))
        all_equipment |= random.choice([{'light crossbow', 'x20 bolts'}, {random.choice(tables.simple_weapons)}])
        return all_equipment
    
    def __str__(self):
        return super().__str__() + f', sorcerous origin: {self.sorcerous_origin}'
    
    def spell_save_dc(self, character):
        return 8 + self.proficiency_bonus + character.stats['Cha'].modifier

    def spell_attack_modifier(self, character):
        return self.proficiency_bonus + character.stats['Cha'].modifier

class Warlock(Class):
    class_name = 'Warlock'
    hit_dice = 8
    spell_slots = 1
    stat_preference = ['Cha', 'Con', 'Int', 'Wis', 'Dex', 'Str']

    def __init__(self):
        super().__init__()
        self.armor_proficiencies.add('light armor')
        self.weapon_proficiencies.add('simple weapons')
        self.skill_proficiencies |= set(random.sample(['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion'], 2))
        self.saving_throws |= {'Wis', 'Cha'}
        self.cantrips |= set(random.sample(tables.warlock_cantrips, 2))
        self.spells |= set(random.sample(tables.warlock_lvl1_spells, 2))
        self.patron = random.choice(['The Archfey', 'The Fiend', 'The Great Old One'])

        if self.patron == 'The Archfey':
            self.class_features.add('Fey Presence')
        elif self.patron == 'The Fiend':
            self.class_features.add('Dark ones Blessing')
        elif self.patron == 'The Great Old One':
            self.class_features.add('Awakened Mind')
    
    def starting_equipment(self):
        all_equipment = {'leather armor', 'x2 dagger'}
        all_equipment |= random.choice([{'light crossbow', 'x20 bolts'}, {'arcane focus'}])
        all_equipment.add(random.choice(tables.simple_weapons))
        all_equipment.add(random.choice(['component pouch', 'arcane focus']))
        all_equipment.add(random.choice(['scholars pack', 'dungeoneers pack']))
        return all_equipment

    def __str__(self):
        return super().__str__() + f', patron: {self.patron}'

    def spell_save_dc(self, character):
        return 8 + self.proficiency_bonus + character.stats['Cha'].modifier

    def spell_attack_modifier(self, character):
        return self.proficiency_bonus + character.stats['Cha'].modifier

class Wizard(Class):
    class_name = 'Wizard'
    hit_dice = 6
    spell_slots = 2
    stat_preference = ['Int', 'Con', 'Dex', 'Cha', 'Wis', 'Str']

    def __init__(self):
        super().__init__()
        self.weapon_proficiencies |= {'daggers', 'darts', 'slings', 'quarterstaff', 'light crossbows'}
        self.skill_proficiencies |= set(random.sample(['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'], 2))
        self.saving_throws |= {'Int', 'Wis'}
        self.class_features.add('Arcane Recovery')
        self.cantrips |= set(random.sample(tables.wizard_cantrips, 3))
        self.spells |= set(random.sample(tables.wizard_lvl1_spells, 6))
        self.arcane_tradition = random.choice(['School of Abjuration', 'School of Conjuration', 'School of Divination', 'School of Enchantment' 'School of Evocation', 'School of Illusion', 'School of Necromancy', 'School of Transmutation'])

        school = self.arcane_tradition.split()[-1]
        self.class_features.add(f'{school} Savant')
    
    def starting_equipment(self):
        all_equipment = {'spellbook'}
        all_equipment.add(random.choice(['quarterstaff', 'dagger']))
        all_equipment.add(random.choice(['component pouch', 'arcane focus']))
        all_equipment.add(random.choice(['scholars pack', 'explorers pack']))
        return all_equipment

    def __str__(self):
        return super().__str__() + f', arcane tradition: {self.arcane_tradition}'
    
    def spell_save_dc(self, character):
        return 8 + self.proficiency_bonus + character.stats['Int'].modifier
    
    def spell_attack_modifier(self, character):
        return self.proficiency_bonus + character.stats['Int'].modifier

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
