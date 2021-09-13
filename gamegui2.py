'''
spanish game gui
April Volzer (amv87)
final project1
May 2019
'''

from tkinter import *
from game2 import *
from random import randint
from word import *

class Gui:
    def __init__(self, window):
        self.game = Game()
        self.window = window
        
        #create canvas
        self.WIDTH = 400
        self.HEIGHT = self.WIDTH
        self.canvas = Canvas (self.window, background = 'white', width = self.WIDTH, height = self.HEIGHT)
        self.canvas.pack()
        
        #start button
        start = Button(window, text="Start", command = self.add_word)
        start.pack(side = BOTTOM)
        
        #input
        self.input = StringVar()
        entry = Entry(window, textvariable = self.input)
        entry.pack(side = BOTTOM)
       
        #error counter
        self.missed = StringVar()
        self.missed.set("0")
        miss_counter = Label(window, textvariable = self.missed, fg = "red")
        miss_counter.pack(side = RIGHT)
        miss_label = Label(window, text = "Missed:", fg = "red")
        miss_label.pack( side = RIGHT)
        
        #score counter
        score_label = Label(window, text = "Score:", fg = "blue")
        score_label.pack(side = LEFT)
        self.score = StringVar()
        self.score.set(0)
        score_counter = Label(window, textvariable = self.score, fg = "blue")
        score_counter.pack(side = LEFT)
        
        #empty word list
        self.word_list = []
        
        self.rate = 50
        
        #check on enter
        root.bind("<Return>", self.process_enter)
        
        self.window.after(0, self.animation)
      
        
    def process_enter(self, event):
        answer = self.input.get()
        self.input.set("")

        if self.game.check_answer(answer) == True:
            self.score.set(int(self.score.get())+ 1)
            self.add_word()
        
    def animation(self):
        '''modified from lab 12 particle simulation'''
        self.canvas.delete("word")
        for word in self.game.word_list:
            #self.text = word
            word.render(self.canvas)
            word.move(self.canvas)
            #add new word when a word is 1/4 of the way down
            if word.get_y() == (self.HEIGHT/4):
                if len(self.game.word_list) < 5:
                    self.add_word()
            #increase error counter when a word hits bottom of canvas
            if word.get_y() > self.HEIGHT:
                self.missed.set(str(int(self.missed.get()) + 1))
                self.game.word_list.pop(0)
        if int(self.missed.get()) < 3:
            self.window.after(self.rate, self.animation)
        else:
            #game over when 3 or more missed
            self.canvas.create_rectangle(0, 0, self.WIDTH, self.HEIGHT, fill = "white")
            self.canvas.create_text(self.WIDTH/2,self.HEIGHT/2,fill="green",font="Times 50 italic bold", text="Game Over")
            #display score
            self.canvas.create_text((self.WIDTH/2)-20, (self.HEIGHT/2)+ 50, font = "Times 20 bold", fill = "green", text = "score:")
            self.canvas.create_text((self.WIDTH/2) + 30, (self.HEIGHT/2)+ 50, font = "Times 20 bold", fill = "green", text = self.score.get())
        

    def add_word(self):
        term = Word(randint(20, self.WIDTH-20),0)
        self.game.word_list.append(term)
        
        
         
if __name__ == "__main__":
    root = Tk()
    root.title("Spanish Quiz")
    app = Gui(root)
    root.mainloop()