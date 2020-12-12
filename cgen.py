import random
import pprint
from random import randint
from character import races

# Choose a character race class
race = random.choice(races)

# Actually construct the character
character = race()
print('stats: ', end='')

pprint.pprint(character.stats)

print('race: ', end='')
pprint.pprint(character.race_name)


# prints the results
#for item in stat_dict:
#    print("{}: {}".format(item,stat_dict[item]))
