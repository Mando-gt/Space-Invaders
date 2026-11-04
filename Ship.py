class Ship:
    CHARACTER = []
    
    def __init__(self, life, damage, bomb, speed):
        self.life = life
        self.damage = damage
        self.speed = speed
        self.bomb = bomb
        self.character = self.CHARACTER
        self.width = len(self.character[0])
        self.length = len(self.character)

    def takeDamage(self, eDamage):
        self.life -= eDamage
