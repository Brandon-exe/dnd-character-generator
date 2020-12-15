import random
import pprint
import character
import classes
import tables

# Choose a character race class
race = random.choice(character.races)
class_ = random.choice(classes.class_list)

# Actually construct the character
character = race(class_)
character_class = class_()
print('stats: ', end='')

pprint.pprint(character.stats)

print('race: ', end='')
pprint.pprint(character.race_name)

print('class: ', end='')
pprint.pprint(class_.class_name)
