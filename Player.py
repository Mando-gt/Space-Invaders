class Player(Ship):
    def __init__(self, life, damage, bomb):
        super().__init__(self, life, damage)
        self.__bomb__ = bomb
        self.__score__ = 0

        def getBomb(self):
            return self.__bomb__

        def setBomb(self, bomb):
            self.__bomb__ = bomb

        
