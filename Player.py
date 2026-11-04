import curses
class Player(Ship):
    def __init__(self, life, damage, bomb, speed, fire_rate):
        super().__init__(self, life, damage)
        self.__bomb__ = bomb
        self.__score__ = 0
        self.__speed__ = speed
        self.__fire_rate__ = fire_rate
        self.__character__ = ["  ^  ", " /_\\ ", "|(O)|", " / \\ "]

        
        
    def getBomb(self):
            return self.__bomb__

    def setBomb(self, bomb):
            self.__bomb__ = bomb

    def setSpeed(self, speed):
        self.__speed__ = speed

    def getSpeed(self):
        return self.__speed__
