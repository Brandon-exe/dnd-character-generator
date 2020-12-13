import random
import pprint
from random import randint
from character import races

# Choose a character race class
race = random.choice(races)
class_ = random.choice(classes)

# Actually construct the character
character = race()
print('stats: ', end='')

pprint.pprint(character.stats)

print('race: ', end='')
pprint.pprint(character.race_name)
