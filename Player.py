import curses
import Ship
class Player(Ship):
    def __init__(self, life, damage, bomb, speed, fire_rate):
        super().__init__(self, life, damage)
        self.score = 0
        self.fire_rate = fire_rate
        self.character = ["  ^  ", " /_\\ ", "|(O)|", " / \\ "]
        self.style = curses.A_REVERSE | curses.A_BOLD
        
