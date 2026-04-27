class Pet:
    def __init__(self, name="Lychee"):
        self.name = name
        self.happiness = 70
        self.growth = 70
        self.health = 70
    
    def get_happiness(self):
        return self.happiness
    
    def increase_happiness(self, amount):
        self.happiness = min(100, self.happiness + amount)
    
    def decrease_happiness(self, amount):
        self.happiness = max(0, self.happiness - amount)

    def get_growth(self):
        return self.growth
    
    def increase_growth(self, amount):
        self.growth = min(100, self.growth + amount)
    
    def decrease_growth(self, amount):
        self.growth = max(0, self.growth - amount)

    def get_health(self):
        return self.health
    
    def increase_health(self, amount):
        self.health = min(100, self.health + amount)
    
    def decrease_health(self, amount):
        self.health = max(0, self.health - amount)

    