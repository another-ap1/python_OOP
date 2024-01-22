"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.word_lst = [word[0:-1] for word in self.file]

    def __repr__(self):
        return f"{len(self.word_lst)} words read"
        
    def random(self):
        return random.choice(self.word_lst)
    
class SpecialWordFinder(WordFinder):

    def __init__(self, file):
        self.file = open(file, 'r')
        self.word_lst = [word[0:-1] for word in self.file]
        for word in self.word_lst:
            if (word == "") or (word[0] == "#"):
                self.word_lst.pop(self.word_lst.index(word))

    def PrintList(self):
        for word in self.word_lst:
            print(word)