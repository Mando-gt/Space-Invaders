from Enemy import Enemy
import curses
class HardEnemy(Enemy):
    CHARACTER = [" .-. ", "( O )", " `-' ", " /|\\ "]
    
    def __init__(self, life, damage, bomb, speed, color=(231,196)):
        super().__init__(self, life, damage, bomb, speed)
        self.color = color
        self.character = self.CHARACTER