import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Word():

    def __init__(self):
        self.secretWord = self.loadWords().lower()
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.length = 9

    def loadWords(self):
        print ("Loading word list from file...")
        self.inFile = open(WORDLIST_FILENAME, 'r')
        self.line = self.inFile.readline()
        self.wordlist = self.line.split(' ')
        print ("  ", len(self.wordlist), "words loaded.")
        return random.choice(self.wordlist)

    def diffCharacters(self):
        while self.length > 8:
            diff = ''.join(set(self.secretWord))
            self.length = len(diff)
        return self.length
