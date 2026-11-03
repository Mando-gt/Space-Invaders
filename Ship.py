class Ship:
    def __init__(self, life, damage):
        self.__life__ = life
        self.__damage__ = damage
        
    def getLife(self):
        return self.__life__
    
    def getDamage(self):
        return self.__daño__
    
    def setLife(self,life):
        self.__life__ = life

    def setDamage(damage):
        self.__damage__ = damage
    
    def takeDamage(self,eDamage):
        setVida(getLife() - eDamage)

