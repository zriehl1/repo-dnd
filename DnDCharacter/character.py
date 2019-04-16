class Character:
    def __init__(self):
        self.sheetMap = {}
        self.maxHP = 0
        self.curHP = 0
        self.proficientSkills = []
        self.abilityScores = [0 for i in range(6)]
        self.passiveWis = 0
        self.otherProficiencies = []
        self.weapons = []
        self.baseArmorClass = 0
        self.items = []
        self.bonds = ""
        self.ideals = ""
        self.personality = ""
        self.flaws = ""
        self.name = ""
        self.alignment = ""
        self.race = ""
        self.charClass = ""
        self.level = 0
        self.background = ""
        self.deathSaves = (0,0)
        self.feats = []
        self.backgroundTraits = []
        self.raceTraits = []
        self.classTraits = []
        self.hitDice = 0
        self.inventory = []

    def loadFromFile(self, filename):
        with open(filename,'r') as cs:
            for line in cs:

    def saveToFile(self, filename):
        None
