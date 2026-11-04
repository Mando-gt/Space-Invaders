import curses
import Enemy
class WeakEnemy(Enemy):
    def __init__(self, life, damage, bomb, speed, color=(231,205)):
        super().__init__(self, life, damage, bomb, speed)
        self.color = color
        self.character = ["^   ^", "|\\_/|", "\\ o /", " \\v/ "]["\\ | /", " \\|/ ", "--@--", "/ | \\"]