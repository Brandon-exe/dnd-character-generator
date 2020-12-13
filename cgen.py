import random
import pprint
import character
import classes
import tables

# Choose a character race class
race = random.choice(character.races)
class_ = random.choice(classes.classes)

# Actually construct the character
character = race()
print('stats: ', end='')

pprint.pprint(character.stats)

print('race: ', end='')
pprint.pprint(character.race_name)
