import curses
from Ship import Ship
class Player(Ship):
    CHARACTER = ["  ^  ", " /_\\ ", "|(O)|", " / \\ "]

    def __init__(self, life, damage, bomb, speed, width, lenght, fire_rate):
        super().__init__(life, damage, bomb, speed, width, length)
        self.score = 0
        self.fire_rate = fire_rate
        self.character = self.CHARACTER
        self.style = curses.A_REVERSE | curses.A_BOLD
        
