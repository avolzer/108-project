'''
word object for spanish game
April Volzer (amv87)
final project1
May 2019
'''

from game2 import *
from tkinter import *

class Word:
    '''based on particle class fom lab 12'''
    
    def __init__(self, x, y):
        self.game = Game()
        self.word = self.game.get_term()
        self.x = x
        self.y = y
        self.speed = 1
        self.rate = 50
        
    def render(self, canvas):
        canvas.create_text(self.x + 10, self.y-10, fill = 'black', text = self.word, tags="word")
        
    def move(self, canvas):
        self.y += self.speed
        
    def get_y(self):
        return self.y
    
    def get_def(self):
        return self.game.get_answer(self.word)
    
    def get_word(self):
        return self.word

    
    
        
