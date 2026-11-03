class Enemy(Ship):
    def __init__(self, life, damage, bomb, speed):
        super().__init__(self, life, damage)
        self.__speed__ = speed
        self.__bomb__ = bomb


