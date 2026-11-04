class Ship:
    def __init__(self, life, damage, bomb, speed):
        self.life = life
        self.damage = damage
        self.speed__ = speed
        self.bomb = bomb
        
    def takeDamage(self, eDamage):
        setVida(self.life - eDamage)
