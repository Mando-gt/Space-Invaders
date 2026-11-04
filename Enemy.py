import Ships
class Enemy(Ship):
    def __init__(self, life, damage, bomb, speed):
        super().__init__(self, life, damage)