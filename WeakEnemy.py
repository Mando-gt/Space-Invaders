import curses
from Enemy import Enemy
class WeakEnemy(Enemy):
    CHARACTER = ["^   ^", "|\\_/|", "\\ o /", " \\v/ "]

    def __init__(self, life, damage, bomb, speed, color=(231,205)):
        super().__init__(self, life, damage, bomb, speed)
        self.color = color
        self.character = self.CHARACTER