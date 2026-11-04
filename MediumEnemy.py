from Enemy import Enemy
import curses
class MediumEnemy(Enemy):
    CHARACTER = [" ,-, ", "(o o)", "(   )", "'~~~'"] 
    
    def __init__(self, life, damage, bomb, speed, color=(231,91)):
        super().__init__(self, life, damage, bomb, speed)
        self.color = color
        self.character = self.CHARACTER