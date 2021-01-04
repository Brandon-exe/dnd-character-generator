import random
import pprint
from .classes import classes
from .races import races
from .backgrounds import backgrounds
from .tables import tables
from .character import Character

race = random.choice(random.choice(races.all))
class_ = random.choice(classes.all)
character_race = race(class_)
character = Character(character_race)
character_class = class_(character)
character.set_class(character_class)

print('stats: ', end='')
pprint.pprint(character.stats)

print('class: ', end='')
pprint.pprint(class_.class_name)

print('race: ', end='')
pprint.pprint(character.race_name)

print('sex: ', end='')
pprint.pprint(character.sex)

print('age: ', end='')
pprint.pprint(character.age)

print('height: ', end='')
pprint.pprint(character.height)

print('weight: ', end='')
pprint.pprint(character.weight)

print('alignment: ', end='')
pprint.pprint(character.alignment)

print('languages: ', end='')
pprint.pprint(character.languages)

print('racial features: ', end='')
pprint.pprint(character.racial_features)

print('class features: ', end='')
pprint.pprint(character.class_features)

print('hit dice: ', end='')
pprint.pprint(character.hit_dice)

print('proficiency bonus: ', end='')
pprint.pprint(character.proficiency_bonus)

print('experience: ', end='')
pprint.pprint(character.experience)

print('armor proficiencies: ', end='')
pprint.pprint(character.armor_proficiencies)

print('weapon proficiencies: ', end='')
pprint.pprint(character.weapon_proficiencies)

print('skill proficiencies: ', end='')
pprint.pprint(character.skill_proficiencies)

print('tool proficiencies: ', end='')
pprint.pprint(character.tool_proficiencies)

print('saving throws: ', end='')
pprint.pprint(character.saving_throws)

print('spell slots: ', end='')
pprint.pprint(character.spell_slots)

print('cantrips: ', end='')
pprint.pprint(character.cantrips)

print('spells: ', end='')
pprint.pprint(character.spells)

print('equipment: ', end='')
pprint.pprint(character.equipment)