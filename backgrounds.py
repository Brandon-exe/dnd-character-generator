import random
import tables


class Background:
    def __init__(self):
        self.skill_proficiencies = set()
        self.tool_proficiencies = set()
        self.languages = set()
        self.features = set()
        self.personality = set()
        self.ideal = set()
        self.bond = set()

class Acolyte(Background):
    background_name = 'Acolyte'

    def __init__(self):
        super().__init__()
        self.skill_proficiencies |= {'Insight', 'Religion'}
        self.languages.add(random.sample(tables.languages, 2))
        self.personality.add(random.choice(tables.acolyte['personality']))
        self.ideal.add(random.choice(tables.acolyte['ideal']))
        self.bond.add(random.choice(tables.acolyte['bond']))
        self.flaw.add(random.choice(tables.acolyte['flaw']))

    def starting_equipment(self):
        all_equipment = {'A Holy Symbol', '15gp', 'x5 Sticks of Incense', 'Vestments', 'Common Cloths'}
        all_equipment.add(random.choice(['Preyer Book', 'Preyer Wheel']))
        return all_equipment

class Charlatan(Background):
    background_name = 'Charlatan'

    def __init__(self):
        super().__init__()
        self.skill_proficiencies |= {'Deception', 'Slight of Hand'}
        self.tool_proficiencies |= {'disguise kit', 'forgery kit'}
        self.scam.add(random.choice(tables.charlatan['favorite scam']))
        self.features.add('false identity')
        self.personality.add(random.choice(tables.charlatan['personality']))
        self.ideal.add(random.choice(tables.charlatan['ideal']))
        self.bond.add(random.choice(tables.charlatan['bond']))
        self.flaw.add(random.choice(tables.charlatan['flaw']))

    def starting_equipment(self):
        all_equipment = {'fine clothes', 'disguise kit', 'x15 gold'}
        
        return all_equipment