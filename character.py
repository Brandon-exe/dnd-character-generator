import random
import tables
import classes
import races
import backgrounds

# rolling the 4d6 for your stat
def roll_stat():
    stat_rolls = 4
    stat = [random.randint(1, 6) for i in range(stat_rolls)]
    stat.sort()
    del stat[0]
    return sum(stat)

class Ability:
    '''A randomly rolled ability score.  Contstructing this rolls it as an ability.'''

    def __init__(self):
        stat_rolls = 4
        stat = [random.randint(1, 6) for i in range(stat_rolls)]
        stat.sort()
        del stat[0]
        self.score = sum(stat)

    @property
    def modifier(self):
        return (self.score - 10) // 2

    # Need to implement lt (less-than) so that this is sortable
    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def __str__(self):
        '''Converts to a string just as an integer'''
        return f'{self.modifier:+} ({self.score})'

    def __repr__(self):
        return f'<Ability {self}>'


def roll_abilities():
    stat_ttl = 6
    all_abilities = [Ability() for i in range(stat_ttl)]
    all_abilities = reversed(sorted(all_abilities))
    return all_abilities

class Character:
    def __init__(self, race):
        self.race = race
        self.sex = random.choice(['Male', 'Female'])
        self.age = random.choice(race.age_range)
        self.height = random.choice(race.height_range)
        self.weight = random.choice(race.weight_range)
        self.alignment = random.choice(tables.alignment)
        self.languages = {'Common'} | race.languages
        self.racial_features = set(race.features)
        self.armor_proficiencies = set(race.armor_proficiencies())

    def set_class(self, class_):
        self.class_ = class_
        self.class_name = (class_.class_name)
        self.class_features = set(class_.features)
        self.hit_dice = (class_.hit_dice)
        self.proficiency_bonus = (class_.proficiency_bonus)
        self.experience = (class_.experience)
        self.armor_proficiencies = set(class_.armor_proficiencies)
        self.weapon_proficiencies = set(class_.weapon_proficiencies)
        self.tool_proficiencies = set(class_.tool_proficiencies)
        self.skill_proficiencies = set(class_.skill_proficiencies)
        self.saving_throws = set(class_.saving_throws)
        self.spell_slots = class_.spell_slots
        self.cantrips = set(class_.cantrips)
        self.spells = set(class_.spells)
        self.equipment = class_.starting_equipment()
        self.stats = dict(zip(class_.stat_preference, roll_abilities()))
