class Enemy(Ship):
    def __init__(self, life, damage, bomb, speed):
        super().__init__(self, life, damage)
        self.__speed__ = speed
        self.__bomb__ = bomb

    def getBomb(self):
            return self.__bomb__

    def setBomb(self, bomb):
            self.__bomb__ = bomb

    def setSpeed(self, speed):
        self.__speed__ = speed

    def getSpeed(self):
        return self.__speed__