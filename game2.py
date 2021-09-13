'''
spanish game
April Volzer amv87
Final project1
May 2019
'''
from random import randint

class Game:
    def __init__(self):
        self.dictionary = {}
        
        f = open("words.txt", 'r')
        lines = f.readlines()
        f.close()
        
        #english-spanish dictionary
        for line in lines:
            x = line.split(' ')
            spanish = x[0]
            english = x[1].rstrip()
            self.dictionary[english] = spanish
        self.english_list = list(self.dictionary.keys())
            
        self.word_list = []
    
    def get_term(self):
        english = self.english_list[randint(0, len(self.english_list)-1)]
        return self.dictionary[english]
    
    def get_answer(self, term):
        self.term = term
        return self.dictionary.get(term)
    
    def check_answer(self, answer):
        if answer in self.dictionary:
            spanish = self.dictionary[answer]
            for word in self.word_list:
                if word.get_word() == spanish:
                    self.word_list.remove(word)
                    return True
            

if __name__ == "__main__":
    test = Game()
    print(test.get_term())
    print(test.get_answer("dinero"))


