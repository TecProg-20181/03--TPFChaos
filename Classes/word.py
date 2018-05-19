import random
import string
import os
import sys

WORDLIST_FILENAME = "palavras.txt"

class Word():

    def __init__(self):
        self.secretWord = ''
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.length = 9
        self.nowords = False

    def loadWords(self):
        print ("Loading word list from file...")
        self.inFile = open(WORDLIST_FILENAME, 'r')
        try:
            if os.stat(WORDLIST_FILENAME).st_size > 0:
               print ("All good")
            else:
               print ("The file is Empty! The game will be ended due to no words being available")
               sys.exit()
        except OSError:
            print ("No file")
        try:
            if WORDLIST_FILENAME.isalpha() == True:
               print ("All good")
            else:
               print ("The file has no words! The game will be ended due to no alphabetic characters being present")
               sys.exit()
        except OSError:
            print ("No file")
        
        self.line = self.inFile.readline()
        self.wordlist = self.line.split(' ')
        
        print ("  ", len(self.wordlist), "words loaded.")
        return random.choice(self.wordlist)

    def diffCharacters(self):
        while self.length > 8:
            diff = ''.join(set(self.secretWord))
            self.length = len(diff)
        return self.length
