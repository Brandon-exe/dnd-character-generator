import random
import pprint
from random import randint
from get_race import get_race

# rolling the 4d6 for your stat
def roll_stat():
    stat_rolls = 4
    stat = [random.randint(1, 6) for i in range(stat_rolls)]
    stat.sort()
    del stat[0]
    return sum(stat)

# loops the roll_stat function to roll 4d6, remove the lowest roll, and repeats 6 times
def stats():
    stat_ttl = 6
    all_stats = [roll_stat() for i in range(stat_ttl)]
    return all_stats

# stores the final stat rolls in a dict with associative stat labels
# This mutates a nonlocal variable
stat_dict = dict(zip(['Str', 'Con', 'Dex', 'Int', 'Wis', 'Cha'], stats()))

race = get_race(stat_dict)
print('stats: ', end='')
pprint.pprint(stat_dict)
print('race: ', end='')
pprint.pprint(race)


# prints the results
#for item in stat_dict:
#    print("{}: {}".format(item,stat_dict[item]))
