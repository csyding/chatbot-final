import random

class Markov(object):
    
    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()
        
    def file_to_words(self):
        """read file and split lines words"""
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words
    
    def quadruples(self):
        """generating 4 words at a time"""
        if len(self.words)<4:
            return
        for i in range(len(self.words)-3):
            yield (words[i], words[i+1], words[i+2], words[i+3])
                
    def database(self):
        for word1, word2, word3, word4 in quadruples(words):
            key = (word1, word2, word3)
            if key in self.cache:
                self.cache[key].append(word4)
            else:
                self.cache[key] = word4
             
               
if __name__ == '__main__':
    Markov().__init__(toot.py)
